# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post, Small_post, Comment
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from django.conf import settings
from g_recaptcha.validate_recaptcha import validate_captcha

from .forms import CommentForm

from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from django.contrib.auth.decorators import login_required
	
from django.contrib.auth import update_session_auth_hash

def post_list(request):
    small_posts = Small_post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'news/post_list.html', {'posts':  reversed(posts), 'small_posts': reversed(small_posts),})

from django.conf import settings
		
@validate_captcha
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # List of active comments for this post
    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.user=request.user.get_username()
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
        else:
            messages.error(request, "Error")
    else:
        comment_form = CommentForm()
    return render(request,
                  'news/post_detail.html',
                 {'post': post,
                  'comments': comments,
				  'form': comment_form,
				  'google_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,})

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибку ниже.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'news/profile/password_change.html', {
        'form': form
    })

def about(request):
    return render(request, 'news/about.html')

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        # Правильный пароль и пользователь "активен"
        auth.login(request, user)
        # Перенаправление на "правильную" страницу
    return render(request, '/')

def logout(request):
    auth.logout(request)
    # Перенаправление на страницу.
    return HttpResponseRedirect("/account/loggedout/")


from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .forms import SignUpForm
from .tokens import account_activation_token

@validate_captcha
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            form.save()
            current_site = get_current_site(request)
            subject = "Активация аккаунта CoinCraft'а"
            message = render_to_string('news/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            messages.success(request, 'Мы отправили инструкции на вашу почту. Если в течении нескольки минут письмо не пришло, проверьте "Спам"')
    else:
        form = SignUpForm()
    return render(request, 'news/signup.html', {'google_key': settings.GOOGLE_RECAPTCHA_SITE_KEY, 'form': form,})

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
        return render(request, 'news/success_reg.html')
    else:
        return render(request, 'news/account_activation_invalid.html')

		
def account_activation_sent(request):
		return render(request, 'news/account_activation_sent.html')		

from django.http import JsonResponse

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)