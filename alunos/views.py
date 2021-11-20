from django.shortcuts import redirect, render

from alunos.forms import AlunoForm
from .models import Aluno
# Create your views here.
def home(request):
    alunos = Aluno.objects.all() #Tras todo mundo na class Aluno
    dados = {
        "alunos":alunos #   "No html":variavel alunos iniciada acima em  alunos = Aluno.objects.all()
    }
    
    return render(request, "home.html", dados)

def cadastro(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)

        if form.is_valid():
            try:
                instancia = form.save(commit=False)
                instancia.save()
                #return redirect('home')  
            except:
                print("Erro ao cadastrar o aluno")      
                
    form = AlunoForm()
    
    dados = {
        "form":form,
    }

    return render(request, "cadastrar.html", dados)    