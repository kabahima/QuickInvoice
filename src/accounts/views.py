from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import UserProfileForm
from django.http import HttpResponse
from .models import Invoice
from .forms import InvoiceForm
from django.contrib import messages

# User registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

# User login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid login credentials')
    return render(request, 'accounts/login.html')

# User profile view - Only accessible by logged-in users
@login_required
def profile(request):
    user = request.user
    return render(request, 'accounts/profile.html', {'user': user})

# User profile edit view
@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'accounts/edit_profile.html', {'form': form})


@login_required
def profile(request):
    user = request.user  # Get the logged-in user
    return render(request, 'accounts/profile.html', {'user': user})

# View to edit the profile of the logged-in user
@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()  # Save the updated user profile
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')  # Redirect to the profile page
    else:
        form = UserProfileForm(instance=user)  # Pre-fill the form with existing data

    return render(request, 'accounts/edit_profile.html', {'form': form})
