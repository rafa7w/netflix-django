from django.urls import path
from .views import Homepage, Homefilmes, Detalhesfilme

urlpatterns = [
    path('', Homepage.as_view()),
    path('filmes/', Homefilmes.as_view()),
    path('filmes/<int:pk>', Detalhesfilme.as_view()),
]