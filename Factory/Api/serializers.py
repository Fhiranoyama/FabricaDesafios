from rest_framework import serializers
from Factory import models

class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Factory
        fields = '__all__'