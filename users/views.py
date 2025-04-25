from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, ProfileUpdateForm
from .models import Profile  # Import Profile model

def register(request):
    """Handles user registration."""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.get_or_create(user=user)  
            login(request, user)  
            return redirect('login')  
    else:
        form = UserRegistrationForm()

    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    """Displays the user's profile information."""
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)  # Ensure profile exists

    return render(request, 'users/profile.html', {
        'user': user,
        'profile': profile
    })

@login_required
def edit_profile(request):
    """Allows users to edit their profile information."""
    user = request.user
    profile, created = Profile.objects.get_or_create(user=user)  # Ensure profile exists

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to profile page after saving
    else:
        form = ProfileUpdateForm(instance=profile)

    return render(request, 'users/edit_profile.html', {'form': form})
