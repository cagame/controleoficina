from django.shortcuts import render, redirect
from .models import Funcionario
from .forms import FuncionarioForm, UsuarioForm
from django.views.generic import ListView, UpdateView, DeleteView, View


class FuncionarioList(ListView):
    model = Funcionario

    def get_queryset(self):
        user = self.request.user.id
        funcionario = Funcionario.objects.get(user=user)
        empresa_logada = funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


def FuncionarioCreate(request):
    funcionarioform = FuncionarioForm(request.POST or None, request.FILES or None)
    usuarioform = UsuarioForm(request.POST or None, request.FILES or None)
    user = request.user.id
    funcionario = Funcionario.objects.get(user=user)
    empresa = funcionario.empresa

    if funcionarioform.is_valid():
       funcionario = funcionarioform.save(commit=False)
       user = usuarioform.save(commit=False)
       user.set_password(user.password)
       user.save()
       funcionario.user = usuarioform.save()
       funcionario.empresa = empresa
       funcionario.save()
       return redirect(FuncionarioCreate)

    return render(request, 'funcionarios/funcionario_form.html', {'funcionarioform': FuncionarioForm, 'usuarioform': UsuarioForm})

class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome']


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = 'funcionario_list'
