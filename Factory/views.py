from django.views import View
from django.http import HttpResponse, JsonResponse
import json
from .models import FactoryModel
import requests

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class Dieta(View):
    def get(self, request):
        nome = request.GET.get('food_name', '')
        site = 'https://caloriasporalimentoapi.herokuapp.com/api/calorias/?descricao={}'.format(nome)
        req = requests.get(site)
        list_of_jsons = req.json()        
        response = HttpResponse()
        response.write("<table>")
        response.write("<tr><th>Descrição</th><th>Quantidade</th><th>Calorias</th></tr>")
        for food in list_of_jsons:
            response.write(f"<tr><td>{food['descricao']}</td><td>{food['quantidade']}</td><td>{food['calorias']}</td></tr>")
        response.write("</table>")
        return response
        

        