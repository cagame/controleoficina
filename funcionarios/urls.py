from django.urls import path
from .views import FuncionarioCreate


urlpatterns = [
    path('novo', FuncionarioCreate.as_view(), name='funcionario_create'),
]