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
        p_name = data.get('descricao')
        p_price = data.get('calorias')
        p_quantity = data.get('quantidade')

        product_data = {
            'product_name': p_name,
            'product_price': p_price,
            'product_quantity': p_quantity,
        }

        cart_item = CartItem.objects.create(**product_data)

        data = {
            "message": f"New item added to Cart with id: {cart_item.id}"
        }
        return JsonResponse(data, status=201)
    

        