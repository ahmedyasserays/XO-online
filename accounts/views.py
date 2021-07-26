from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm
from accounts.decorators import *

# Create your views here.
@restrict_logged
def sign_up(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('app:online')

    return render(request, 'accounts/signup.html', {'form':form})

@restrict_logged
def log_in(request):
    if request.method == 'POST':
        user = authenticate(request, email=request.POST.get('email'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return redirect('app:online')
    return render(request, 'accounts/login.html')

@restrict_unlogged
def profile(request):
    return render(request, 'accounts/profile.html')

@restrict_unlogged
def settings(request):
    return render(request, 'accounts/settings.html')