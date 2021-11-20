from django import forms
from django.forms import ModelForm
from django import forms
from .models import Aluno

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'