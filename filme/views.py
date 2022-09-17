from django.shortcuts import redirect
from django.shortcuts import render
from .models import Categoria, Titulo
from .forms import TituloForm

def home(request):
    data = {}
    return render(request, 'filme/home.html')

def listagem(request):
    data = {}
    data['listagem'] = Titulo.objects.all()
    return render(request, 'filme/listagem.html', data)

def novo_titulo(request):
    data = {}
    form = TituloForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect("listagem")
        
    data['form'] = form
    return render(request, 'filme/form.html', data)

def update(request, pk):
    data = {}
    titulo = Titulo.objects.get(pk=pk)
    form = TituloForm(request.POST or None, instance=titulo)
    
    if form.is_valid():
        form.save()
        return redirect("listagem")
        
    data['form'] = form
    data['titulo'] = titulo
    return render(request, 'filme/form.html', data)

def delete(request, pk):
    filme = Titulo.objects.get(pk=pk)
    filme.delete()
    return redirect("listagem")
