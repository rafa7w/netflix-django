from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
# url -> view -> template

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
  # o que é passado para o front é um object_list (lista de itens do modelo)

class Detalhesfilme(DetailView):
  template_name = 'detalhesfilme.html'
  model = Filme
  # object -> um item do nosso modelo

  def get(self, req, *args, **kwargs):
    # contabilizando
    filme = self.get_object()
    filme.visualizacoes +=1
    filme.save()
    return super().get(req, *args, **kwargs) # redireciona o usuário para a url final

  # O context no Class Based Views já é criado automaticamente
  def get_context_data(self, **kwargs):
    context = super(DetailView, self).get_context_data(**kwargs)

    # filtrar a tabela de filmes, cuja categoria é igual
    filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[:5]
    context['filmes_relacionados'] = filmes_relacionados
    return context

class Pesquisafilme(ListView):
  template_name = 'pesquisa.html'
  model = Filme

  def get_queryset(self):
    termo_pesquisa = self.request.GET.get('query')
    if termo_pesquisa:
      object_list = self.model.objects.filter(titulo__icontains=termo_pesquisa)
      return object_list
    else:
      return None