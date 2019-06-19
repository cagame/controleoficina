from django.urls import path
from .views import Municipio


urlpatterns = [
    path('', Municipio, name='municipio'),
]