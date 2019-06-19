from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Funcionario
from .forms import FuncionarioForm
from empresas.models import Empresa
from django.contrib.auth.models import User


class FuncionarioCreate(CreateView):
    model = Funcionario
    form_class = FuncionarioForm

    def form_valid(self, form):
            funcionario = form.save(commit=False)
            funcionario.empresa = Empresa.objects.create(nome=empresa)
            funcionario.user = User.objects.create_user(username=usuario, password=senha)
            funcionario.save()
            return super(FuncionarioCreate, self).form_valid(form)