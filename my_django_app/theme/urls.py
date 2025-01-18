from django.contrib import admin
from django.urls import path
from theme import views

app_name ='theme'

urlpatterns = [
    path('', views.index, name='index')
]