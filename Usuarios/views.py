from django.shortcuts import render, redirect, get_object_or_404
from .models import Professor, Aluno, Turma, Avaliacao, Nota

def home_alunos(request):
    registro = Nota.objects.select_related('avaliacao').all() 
    return render(request, 'home_alunos.html', {'registro':registro})

def home_admin(request):
    return render(request, 'home_admin.html')

def lista_admin(request):
    tipo = request.GET.get('tipo', 'registros') 
    if tipo == 'alunos':
        registros = Aluno.objects.select_related('turma').all()
    else:
        registros = Professor.objects.all()
    return render(request, 'lista_admin.html', {'registros': registros, 'tipo': tipo})

def home_professores(request):
    return render(request, 'home_professores.html')

