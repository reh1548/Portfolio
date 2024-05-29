from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm


def registerUser(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('index'))
        else:
            messages.error(request, "Invalid Format!")
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/login_register.html', {'form': form, 'register': True})

def loginUser(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))  # Redirect to home page if the user is already logged in

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "User Name doesn't exist")
            return render(request, 'accounts/login_register.html')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Log in the user
            return redirect(reverse('index'))  # Redirect to home page after successful login
        else:
            messages.error(request, 'User Name or Password is incorrect')

    return render(request, 'accounts/login_register.html')


def logoutUser(request):
    logout(request)
    messages.success(request, 'User logged out')
    return redirect('login')
