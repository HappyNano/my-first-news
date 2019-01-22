# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from .models import ForumBlock,ForumSubBlock,ForumPost,Comment

from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse

from .forms import PostForm, CommentForm

from django.conf import settings
from g_recaptcha.validate_recaptcha import validate_captcha

from django.contrib.auth.models import User

from django.contrib.auth.decorators import user_passes_test

def group_required(*group_names):
   """Requires user membership in at least one of the groups passed in."""

   def in_groups(u):
       if u.is_authenticated():
           if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
               return True
       return False
   return user_passes_test(in_groups)

@login_required
def forum(request):
    blocks = ForumBlock.objects.filter(active=True)
    subblocks = ForumSubBlock.objects.filter(active=True)
    return render(request, 'forum/forum.html',  {'blocks':  blocks, 'subblocks': subblocks,})

@login_required
def block(request, pk):
    block = get_object_or_404(ForumSubBlock, pk=pk)
    posts = block.post.filter()

    return render(request, 'forum/block.html', {'posts1': reversed(posts), 'posts2': reversed(posts), 'subblock': block,})

@login_required
@validate_captcha
def post_detail(request, pk):
    post = get_object_or_404(ForumPost, pk=pk)
    # List of active comments for this post
    comments = post.comments.filter(active=True)
    if request.user.username not in post.views:
        post.views += str(request.user.username) + ' '
        post.save()

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid() and post.active == True:
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.user = request.user.get_username()
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
        else:
            messages.error(request, "Ошибка")
    else:
        comment_form = CommentForm()
    return render(request,
                  'forum/post_detail.html',
                 {'User': User.objects.all(),
				  'post': post,
                  'comments': comments,
				  'form': comment_form,
				  'google_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,})

@login_required
def post_add(request, pk):
    if request.method == 'POST':
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.author = User.objects.get(username=request.user.username)
            new_post.block = get_object_or_404(ForumSubBlock, pk=pk)
            new_post.save()
            return redirect('/forum/post/{0}'.format(new_post.pk),)
        else:
            messages.error(request, "Ошибка")
    else:
        post_form = PostForm(instance=request.user)
    return render(request,
                  'forum/post_add.html',
                 {
				  'post_form': post_form,
				  'google_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,})

@login_required
@group_required("forum_moderator")
def checking(request):
    posts = ForumPost.objects.all().filter()
    return render(request, 'forum/check.html', {'posts': reversed(posts)})

@login_required
@group_required("forum_moderator")
def check(request):
    pk = request.GET.get('pk', None)
    do = int(request.GET.get('do', None))
    if do == 1 or do == 0:
        if do == 1:
            do = True
        if do == 0:
            do = False
        post = get_object_or_404(ForumPost, pk=pk)
        post.checked = do
        post.save()
    return JsonResponse({'1': '1'})

@login_required
@permission_required('forum.forum.post.close')
def close(request):
    pk = request.GET.get('pk', None)
    do = int(request.GET.get('do', None))
    if do == 1 or do == 0:
        if do == 1:
            do = True
        if do == 0:
            do = False
        post = get_object_or_404(ForumPost, pk=pk)
        post.active = do
        post.save()
    return JsonResponse({'1': '1'})

@login_required
def delete(request):
    pk = request.GET.get('pk', None)
    post = get_object_or_404(ForumPost, pk=pk)
    if request.user.has_perm('forum.forum.post.delete.foreign') or post.author.username == request.user.username:
        post.delete()
    return JsonResponse({'1': '1'})