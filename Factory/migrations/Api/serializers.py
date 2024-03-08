from rest_framework import serializers
from Factory import models

class FactorySerializer(serializers.modelSerializer):
    class Meta:
        model = models.Factory
        fields = '__all__'