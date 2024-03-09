from rest_framework import viewsets
from Factory.Api import serializers
from Factory import models

class FactoryViewsSet(viewsets.ModelViewSet):
    serializer_class = serializers.FactorySerializer
    queryset = models.Factory.objects.all()