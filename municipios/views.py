import requests
from django.http import JsonResponse

def listar_municipios(request):
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/26/municipio'
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        cidades = [cidade['nome'] for cidade in dados]
        return JsonResponse({'cidades': cidades})
    else:
        return JsonResponse({'erro': 'Não foi possível acessar a API do IBGE'}, status=500)