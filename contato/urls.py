from django.urls import path
from django.contrib import admin
from .views import emailView, successView


urlpatterns = [
    path('email/', emailView, name='email'),
    path('sucess/', successView, name='sucess'),
]