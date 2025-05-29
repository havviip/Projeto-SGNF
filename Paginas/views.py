from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def login_admin(request):
    return render(request, 'login_admin.html')