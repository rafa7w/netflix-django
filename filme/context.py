from .models import Filme

def lista_filmes_recentes(req):
  lista_filmes = Filme.objects.all().order_by('-data_criacao')[:10]
  return {'lista_filmes_recentes': lista_filmes}

def lista_filmes_emalta(req):
  lista_filmes = Filme.objects.all().order_by('-visualizacoes')[:10]
  return {'lista_filmes_emalta': lista_filmes}

