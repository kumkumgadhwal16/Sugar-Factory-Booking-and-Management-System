"""
accounts/views.py
User registration, login, logout, profile update.
"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm, UserProfileForm
from .models import User, UserProfile


def register_view(request):
    """User Registration ."""
    if request.user.is_authenticated:
        return redirect('booking:dashboard')

    form = UserRegistrationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully! Please update your profile.')
            return redirect('accounts:update_profile')
        else:
            messages.error(request, 'Please correct the errors below.')

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    """User Login """
    if request.user.is_authenticated:
        return redirect('booking:dashboard')

    form = UserLoginForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.email}!')
                next_url = request.GET.get('next', 'booking:dashboard')
                return redirect(next_url)
        messages.error(request, 'Invalid email or password.')

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    """Logout."""
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('core:home')


@login_required
def update_profile_view(request):
    """Update farmer profile"""
    profile, created = UserProfile.objects.get_or_create(
        user=request.user,
        defaults={'email': request.user.email, 'fname': '', 'lname': '', 'phone': ''}
    )

    form = UserProfileForm(request.POST or None, instance=profile)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('booking:dashboard')
        else:
            messages.error(request, 'Please correct the errors below.')

    return render(request, 'accounts/update_profile.html', {
        'form': form,
        'profile': profile,
    })
