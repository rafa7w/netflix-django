from django.shortcuts import render
from .models import Filme

# Create your views here.
def homepage(req):
  return render(req, 'homepage.html')

def homefilmes(req):
  context = {}
  lista_filmes = Filme.objects.all()
  context['lista_filmes'] = lista_filmes
  return render(req, 'homefilmes.html', context)