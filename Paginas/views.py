from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login_aluno(request):
    return render(request, 'login_aluno.html')

def login_professor(request):
    return render(request, 'login_professor.html')

def login_admin(request):
    return render(request, 'login_admin.html')

def cadastro_aluno(request):
    return render(request, 'cadastro_aluno.html')

def cadastro_professor(request):
    return render(request, 'cadastro_professores.html')

def cadastro_turma(request):
    return render(request, 'cadastro_turma.html')

def editar_aluno(request):
    return render(request, 'editar_aluno.html')

def cadastro_avaliacao(request):
    return render(request, 'cadastro_avaliacao.html')

def lanca_nota(request):
    return render(request, 'lanca_nota.html')