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
    
    def post(self, request):

        data = json.loads(request.body.decode("utf-8"))
        descricao = data.get('descricao')
        calorias = data.get('calorias')
        quantidade = data.get('quantidade')

        produco_data = {
            'descricao': descricao,
            'calorias': calorias,
            'quantidade': quantidade,
        }

        food_item = FactoryModel.objects.create(**produco_data)

        data = {
            "message": f"food_name: {food_item.id}"
        }
        return JsonResponse(data, status=201)
    
@method_decorator(csrf_exempt, name='dispatch')
class updel(View):

    def patch(self, request, item_id):
        data = json.loads(request.body.decode("utf-8"))
        item = FactoryModel.objects.get(id=item_id)
        item.quantidade= data['quantidade_de_comida']
        item.save()

        data = {
            'message': f'Item {item_id} has been updated'
        }

        return JsonResponse(data)


    def delete(self, request, item_id):
        item = FactoryModel.objects.get(id=item_id)
        item.delete()

        data = {
            'message': f'Item {item_id} Food has been removed!'
        }

        return JsonResponse(data)
    

