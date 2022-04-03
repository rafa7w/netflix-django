from .models import Filme

def lista_filmes_recentes(req):
  lista_filmes = Filme.objects.all().order_by('-data_criacao')[:8]
  filme_destaque = lista_filmes[0]
  return {'lista_filmes_recentes': lista_filmes, 'filme_destaque': filme_destaque}

def lista_filmes_emalta(req):
  lista_filmes = Filme.objects.all().order_by('-visualizacoes')[:8]
  return {'lista_filmes_emalta': lista_filmes}