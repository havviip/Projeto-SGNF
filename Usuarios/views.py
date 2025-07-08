from django.shortcuts import render

def home_alunos(request):
    return render(request, 'home_alunos.html')

def home_admin(request):
    return render(request, 'home_admin.html')

def lista_admin(request):
    return render(request, 'lista_admin.html')

def home_professores(request):
    return render(request, 'home_professores.html')