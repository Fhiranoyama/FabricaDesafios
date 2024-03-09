from django.db import models


class FactoryModel(models.Model):
    descricao = models.CharField(verbose_name="descricao", max_length=40)
    calorias = models.CharField(verbose_name="calorias", max_length=40)
    quantidade = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.descricao} {self.calorias}" 