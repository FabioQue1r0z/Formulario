from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    idade = models.IntegerField()


    def __str__(self):
        return self.nome