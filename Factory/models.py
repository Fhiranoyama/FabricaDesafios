from django.db import models
from uuid import uuid4

class Factory(models.model):

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(verbose_name="nome", max_length=255)
    data = models.CharField(verbose_name="data", max_length=255)
    quantidade = models.datefield(auto_now_add=True)
    calorias = models.CharField(verbose_name="calorias", max_length=255)