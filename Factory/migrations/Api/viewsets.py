from rest_framework import viewsets
from Factory.api import serializers
from Factory import models

class FactoryViewsSet(viewsets.ModelViewSet):
    serializer_class = serializer.FactorySerializer
    queryset = models.Factory.objects.all()