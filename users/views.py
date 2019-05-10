from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic.edit import CreateView

from .models import User, Profile
from .forms import UserForm, ProfileForm


# Create your views here.
@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, _('Your profiles was successfully updated!'))
            return redirect('main')
        else:
            messages.error(request, _('Please correct the error below.'))

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'users/profiles/profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def create_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            messages.success(request, _('Your profiles was successfully updated!'))
            return redirect('main')
        else:
            messages.error(request, _('Please correct the error below.'))
    elif request.method == 'GET':
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'users/profiles/signup.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
