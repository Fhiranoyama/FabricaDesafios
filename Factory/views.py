from django.shortcuts import render

import requests

def get_calorias(request, nome_alimento):
    #nome = request.data.get('name', '')
    site = 'https://caloriasporalimentoapi.herokuapp.com/api/calorias/?descricao={}'.format(nome_alimento)
    req = requests.get(site)
    json = req.json()
    print(json)
    return json