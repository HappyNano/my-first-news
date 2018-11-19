# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from .models import ForumBlock,ForumSubBlock,ForumPost,Comment

from .forms import CommentForm

from django.conf import settings
from g_recaptcha.validate_recaptcha import validate_captcha

def forum(request):
    blocks = ForumBlock.objects.filter(active=True)
    subblocks = ForumSubBlock.objects.filter(active=True)
    return render(request, 'forum/forum.html',  {'blocks':  blocks, 'subblocks': subblocks,})

def block(request, pk):
    block = get_object_or_404(ForumSubBlock, pk=pk)
    posts = block.post.filter(active=True)

    return render(request, 'forum/block.html', {'posts': posts,})

@validate_captcha
def post_detail(request, pk):
    post = get_object_or_404(ForumPost, pk=pk)
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
            messages.error(request, "Ошибка")
    else:
        comment_form = CommentForm()
    return render(request,
                  'forum/post_detail.html',
                 {'post': post,
                  'comments': comments,
				  'form': comment_form,
				  'google_key': settings.GOOGLE_RECAPTCHA_SITE_KEY,})