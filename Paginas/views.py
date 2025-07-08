from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def login_admin(request):
    return render(request, 'login_admin.html')

def cadastro_aluno(request):
    return render(request, 'cadastro_aluno.html')

def cadastro_professor(request):
    return render(request, 'cadastro_professores.html')

def cadastro_disciplina(request):
    return render(request, 'cadastro_disciplina.html')