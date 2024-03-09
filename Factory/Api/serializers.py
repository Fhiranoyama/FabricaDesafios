from rest_framework.serializers import ModelSerializer
from ..models import FactoryModel

class FactorySerializer(ModelSerializer):
    class Meta:
        model = FactoryModel
        fields = ['id', 'descricao', 'calorias']