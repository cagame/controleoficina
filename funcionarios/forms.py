from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Funcionario


class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome']


class UsuarioForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
