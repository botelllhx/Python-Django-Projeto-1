from django.shortcuts import render
from utils.recipes.factory import make_recipe
from django.http import HttpResponse


def home(request):
    return render(request, 'receitas/pages/home.html', context={
        'name': 'Mateus Botelho',
        'recipes': [make_recipe() for _ in range(10)],
    })

def receita(request, id):
   return render(request, 'receitas/pages/recipe-view.html', context={
        'name': 'Mateus Botelho',
        'recipe': make_recipe(),
    })
