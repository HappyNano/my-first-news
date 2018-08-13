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
import logging
logger = logging.getLogger(__name__)

def post_list(request):
    ip = request.META.get('REMOTE_ADDR', '') or request.META.get('HTTP_X_FORWARDED_FOR', '')
    logger.debug('USER: '+str(request.user.username)+' IP: '+str(ip)+' post_list')
    small_posts = Small_post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'news/post_list.html', {'posts':  reversed(posts), 'small_posts': reversed(small_posts),})

from django.conf import settings
		
@validate_captcha
def post_detail(request, pk):
    ip = request.META.get('REMOTE_ADDR', '') or request.META.get('HTTP_X_FORWARDED_FOR', '')
    logger.debug('USER: '+str(request.user.username)+' IP: '+str(ip)+' post_detail')
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
            new_comment.user = request.user.get_username()
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

def about(request):
    ip = request.META.get('REMOTE_ADDR', '') or request.META.get('HTTP_X_FORWARDED_FOR', '')
    logger.debug('USER: '+str(request.user.username)+' IP: '+str(ip)+' about')
    return render(request, 'news/about.html')

def login(request):
    ip = request.META.get('REMOTE_ADDR', '') or request.META.get('HTTP_X_FORWARDED_FOR', '')
    logger.debug('USER: '+str(request.user.username)+' IP: '+str(ip)+' login')
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

from django.http import JsonResponse

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)