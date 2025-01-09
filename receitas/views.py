from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'receitas/pages/home.html')

def receita(request):
    return render(request, 'receitas/pages/home.html')
