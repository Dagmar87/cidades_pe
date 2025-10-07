from django.urls import path
from .views import listar_municipios

urlpatterns = [
    path('cidades/', listar_municipios, name='listar_municipios'),
]