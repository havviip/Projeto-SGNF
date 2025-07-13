from django.shortcuts import render, redirect, get_object_or_404
from .models import Professor, Aluno

def home_alunos(request):
    return render(request, 'home_alunos.html')

def home_admin(request):
    return render(request, 'home_admin.html')

def lista_admin(request):
    tipo = request.GET.get('tipo', 'registros') 
    if tipo == 'alunos':
        registros = Aluno.objects.all()
    else:
        registros = Professor.objects.all()
    return render(request, 'lista_admin.html', {'registros':registros, 'tipo':tipo})

def home_professores(request):
    return render(request, 'home_professores.html')

