from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from empresas.forms import EmpresaForm
from funcionarios.forms import FuncionarioForm, UsuarioForm


def registro(request):
    empresaform = EmpresaForm(request.POST or None, request.FILES or None)
    funcionarioform = FuncionarioForm(request.POST or None, request.FILES or None)
    usuarioform = UsuarioForm(request.POST or None, request.FILES or None)
    if funcionarioform.is_valid() and empresaform.is_valid() and usuarioform.is_valid():
        funcionario = funcionarioform.save(commit=False)
        empresa = empresaform.save()
        user = usuarioform.save(commit=False)
        user.set_password(user.password)
        user.save()
        funcionario.empresa = empresa
        funcionario.user = user
        funcionario.save()

        return redirect(home)

    return render(request, 'registro.html', {'funcionarioform': funcionarioform, 'empresaform': empresaform,
                                             'usuarioform': usuarioform})

@login_required
def home(request):
    return render(request, 'index.html')
