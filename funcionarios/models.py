from django.db import models
from django.contrib.auth.models import User
from empresas.models import Empresa
from django.urls import reverse


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('list_departamentos')
