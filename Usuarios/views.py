from django.shortcuts import render

def home_alunos(request):
    return render(request, 'home_alunos.html')

def home_admin(request):
    return render(request, 'home_admin.html')