from msilib.schema import ListView
from re import template
from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView

# Create your views here.
# def homepage(req):
#   return render(req, 'homepage.html')

class Homepage(TemplateView):
  template_name = 'homepage.html'

#def homefilmes(req):
#  context = {}
#  lista_filmes = Filme.objects.all()
#  context['lista_filmes'] = lista_filmes
#  return render(req, 'homefilmes.html', context)

class Homefilmes(ListView):
  template_name = 'homefilmes.html'
  model = Filme
  # o que é passado para o front é um object_list