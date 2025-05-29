from django.shortcuts import render

def home_alunos(request):
    return render(request, 'home_usuarios.html')