# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.models import User

from django.db import transaction
"""
@login_required
def profile(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST)
        if form.is_valid():
            new_avatar = form.save(commit=False)
            new_avatar.user=request.user
            new_avatar.save()
        else:
            messages.error(request, "Error")
    else:
        avatar_form = AvatarForm(instance=request.user.profile)
    return render(request, 'userprofile/profile/profile.html')
"""

@login_required
def update_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('/lk/profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'userprofile/profile/profile.html', {
        'profile_form': profile_form
    })