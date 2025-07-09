from django.shortcuts import render, redirect

def login(request):
     return render(request, 'authentication/templates/login_logs.html')
