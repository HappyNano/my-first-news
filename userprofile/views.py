# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import AvatarForm, ProfileForm,  UserForm
from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .forms import SignUpForm
from .tokens import account_activation_token
from django.conf import settings

from django.db import transaction
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from g_recaptcha.validate_recaptcha import validate_captcha

from django.http import JsonResponse
import logging, json
logger = logging.getLogger(__name__)

from django.contrib.auth import login, authenticate

def login(request):
    username = request.POST.get('username', "")
    password = request.POST.get('password', "")
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
    else:
        messages.error(request, '''<script type="text/javascript" id="message-script">
				$("fieldset#box").slideToggle(0);
				$("div#log-head").slideToggle(0);
				swal({
					icon: "error",
					text: "Логин или пароль не совпадают! Попробуйте заного",
					closeOnClickOutside: false,
				});
				$("#message-script").remove();
			</script><div style="color:red;">Логин или пароль не совпадают! Попробуйте заного</div>''')
    return redirect('/')

def logout(request):
    auth.logout(request)
    # Перенаправление на страницу.
    return redirect('/')

from django.core.mail import send_mail
@validate_captcha
def signup(request):
    ip = request.META.get('REMOTE_ADDR', '') or request.META.get('HTTP_X_FORWARDED_FOR', '')
    logger.debug('USER: '+str(request.user.username)+' IP: '+str(ip)+' signup')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            form.save()
            current_site = get_current_site(request)
            subject = "Активация аккаунта CoinCraft'а"
            html = render_to_string('userprofile/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            send_mail(
    subject,
    '.',
    settings.EMAIL_HOST_USER,
    [user.email],
    html_message=html,)
            messages.success(request, 'Мы отправили инструкции на вашу почту. Если в течении нескольки минут письмо не пришло, проверьте "Спам"')
    else:
        form = SignUpForm()
    return render(request, 'userprofile/signup.html', {'google_key': settings.GOOGLE_RECAPTCHA_SITE_KEY, 'form': form,})

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        return render(request, 'userprofile/success_reg.html')
    else:
        return render(request, 'userprofile/account_activation_invalid.html')	

def change_password(request):
    ip = request.META.get('REMOTE_ADDR', '') or request.META.get('HTTP_X_FORWARDED_FOR', '')
    logger.debug('USER: '+str(request.user.username)+' IP: '+str(ip)+' change_password')
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Ваш пароль был успешно изменен!')
            return redirect('change_password')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибку ниже.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'userprofile/profile/password_change.html', {
        'form': form
    })

@login_required
def profile(request):	
    return render(request, 'userprofile/profile/profile.html')

@login_required
@transaction.atomic
def edit_profile(request):
    ip = request.META.get('REMOTE_ADDR', '') or request.META.get('HTTP_X_FORWARDED_FOR', '')
    logger.debug('USER: '+str(request.user.username)+' IP: '+str(ip)+' update_profile')
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, ('Ваш профиль был успешно изменен!'))
            return redirect('/account/profile')
        else:
            messages.error(request, ('Пожалуйста, исправьте ошибку ниже.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'userprofile/profile/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def update_avatar(request):
    ip = request.META.get('REMOTE_ADDR', '') or request.META.get('HTTP_X_FORWARDED_FOR', '')
    logger.debug('USER: '+str(request.user.username)+' IP: '+str(ip)+' update_avatar')
    if request.method == 'POST':
        avatar_form = AvatarForm(request.POST, instance=request.user.profile)
        if avatar_form.is_valid():
            myfile = request.FILES['avatar']
            mb_limit = 5.0
            if myfile.size > mb_limit*1024*1024:
                messages.error(request, ("Размер загружаемого аватара не может превышать %sMB" % str(mb_limit)))
            else:
                new_avatar = avatar_form.save(commit=False)
                new_avatar.avatar = myfile
                new_avatar.save()
                messages.success(request, ('Новый аватар был загружен!'))
            return redirect('/account/profile')
        else:
            messages.error(request, ('Ошибка'))
    else:
        avatar_form = AvatarForm(instance=request.user.profile)
    return render(request, 'userprofile/profile/profile.html')

def get_avatar(request):
    username = request.GET.get('username', None)
    user = User.objects.get(username=username)
    data = {
        'avatar': user.profile.avatar.url
    }
    return JsonResponse(data)