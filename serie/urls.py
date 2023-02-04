from django.contrib import admin
from django.urls import path, include
from .views import detalhes_serie, cadastra_serie, cadastra_temporada, cadastra_episodio, detalhes_episodio

app_name = 'serie'

urlpatterns = [
    path('<int:serie>', detalhes_serie, name="detalhes_serie"),
    path('cadastra/', cadastra_serie, name="cadastra_serie"),
    path('cadastra_temporada/', cadastra_temporada, name="cadastra_temporada"),
    path('cadastra_episodio/<int:serie>', cadastra_episodio, name="cadastra_episodio"),
    path('detalhes_episodio/<int:episodio>', detalhes_episodio, name="detalhes_episodio"),
]