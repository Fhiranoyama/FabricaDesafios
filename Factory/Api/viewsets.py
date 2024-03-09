from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from  ..models import FactoryModel
from .serializers import FactorySerializer
import requests



class FactoryViewSet(ModelViewSet):
    queryset = FactoryModel.objects.all()
    serializer_class = FactorySerializer

    def create(self, request):
    # Use request.data para obter os dados da solicitação HTTP
        nome = request.data.get('descricao', 'calorias')
        site = (f'https://caloriasporalimentoapi.herokuapp.com/api/calorias/?descricao={nome}')
        requisicao = requests.get(site)
        json = requisicao.json()

        descricao = json.get('descricao', '')
        calorias = json.get('calorias', '')
  

        dadosrecebidos = {
            "descricao": f"{descricao}",
            "calorias": f"{calorias}",

        }
        

        meuserializer = FactorySerializer(data=dadosrecebidos)
        if meuserializer.is_valid():
            meuserializer.save()
            return Response(meuserializer.data)
               
        else:
            return Response({"aviso": "erro da um jeito"})
