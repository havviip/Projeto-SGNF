from django.db import models
from django.db.models import Count, Avg


class Professor(models.Model):
    id_professor = models.IntegerField(primary_key=True)
    nomeProfessor = models.CharField(max_length=100)
    senha_professor = models.CharField(max_length=15)
    matriculaProfessor = models.IntegerField(unique=True)
    
    class Meta: 
        managed = False
        db_table = 'professor'

    def __str__(self):
        return self.nomeProfessor

class Turma(models.Model):
    id_turma = models.IntegerField(primary_key=True)
    nome_turma = models.CharField(max_length=50)
    ano = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'turma'

    def __str__(self):
        return self.nome_turma

class Aluno(models.Model):
    id_aluno = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=50)
    turma = models.ForeignKey(
        Turma,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        db_column = 'id_turma'
    )

    class Meta:
        managed = False
        db_table = 'aluno'

    def __str__(self):
        return self.nome
    
class Avaliacao(models.Model):
    id_avaliacao = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'avaliacao'

    def __str__(self):
        return self.tipo

    
class Nota(models.Model):
    id_nota = models.IntegerField(primary_key=True)
    valor = models.FloatField()
    avaliacao = models.ForeignKey(
        Avaliacao,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        db_column = 'id_avaliacao'
    )
    aluno= models.ForeignKey(
        Aluno,
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        db_column = 'id_aluno'
    )

    class Meta:
        managed = False
        db_table = 'nota'

    def __str__(self):
        return self.id_nota
    




