from django.db import models

# Create your models here.
class Estado(models.Model):
    nome = models.CharField(max_length=2)

    def __str__(self):
        return self.nome


class Municipio(models.Model):
    estado = models.ForeignKey(Estado, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome