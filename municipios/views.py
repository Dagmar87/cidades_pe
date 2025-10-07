import requests
from django.shortcuts import render
#from django.http import JsonResponse

def listar_municipios(request):
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/26/municipios'
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        cidades = [cidade['nome'] for cidade in dados]
        return render(request, 'municipios/lista_cidades.html', {'cidades': cidades})
    else:
        return render(request, 'municipios/lista_cidades.html', {'erro': 'Erro ao acessar a API'})