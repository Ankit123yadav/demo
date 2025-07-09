from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def login(request):
    if request.user.is_authenticated:
        return redirect('admindashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('admindashboard')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')
    return redirect('login')
   

@login_required
def home(request):
    return render(request, 'base.html')  # template path

@login_required
def admindashboard(request):
    return render(request, 'core/dashboard/admindashboard.html')

@login_required
def logout(request):
    auth_logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')
