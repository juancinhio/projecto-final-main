from django.db import models


class Frenos(models.Model):

    nombre = models.CharField(max_length=100, null=True, blank=True)
    cantidad = models.CharField(max_length=100, null=True, blank=True)
    pedidos = models.CharField(max_length=100, null=True, blank=True)
    ok = models.BooleanField(null=True, blank=True)

    @staticmethod
    def get_default_nombres():
        return ['Valor 1', 'Valor 2', 'Valor 3', 'Valor 4', 'Valor 5']


class Servicios(models.Model):
    frenos = models.ForeignKey(Frenos, on_delete=models.CASCADE)