from django.urls import path
from .views import FuncionarioCreate, FuncionarioList, FuncionarioEdit, FuncionarioDelete


urlpatterns = [
    path('novo', FuncionarioCreate, name='funcionario_create'),
    path('list', FuncionarioList.as_view(), name='funcionario_list'),
    path('edit/<int:pk>/', FuncionarioEdit.as_view(), name='funcionario_update'),
    path('delete/<int:pk>/', FuncionarioDelete.as_view(), name='funcionario_delete'),
]