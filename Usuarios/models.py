from django.db import models


class Professor(models.Model):
    id_professor = models.IntegerField(primary_key=True)
    nomeProfessor = models.CharField(max_length=100)
    senha_professor = models.CharField(max_length=15)
    matriculaProfessor = models.IntegerField(unique=True)
    
    class Meta: 
        managed = False
        db_table = 'professor'

    def __str__(self):
        return self.nome_professor
    
class Aluno(models.Model):
    id_aluno = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'aluno'

    def __str__(self):
        return self.nome
