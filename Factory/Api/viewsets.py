from rest_framework import viewsets
from Factory.Api import serializers
from Factory import models

import requests


class FactoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FactorySerializer
    queryset = models.Factory.objects.all()

def create(self, request):
    nome = request.data.get('name', '')
    site = 'https://caloriasporalimentoapi.herokuapp.com/api/calorias/?descricao={}'.format(nome)
    req = requests.get(site)
    json = req.json()
    print(json)