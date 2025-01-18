"""
URL configuration for my_django_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from theme.views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('help/', help, name='help'),
    path('login/', login, name='login'),
    path('process/', process_form, name='process_form'),

    path('bio_motor/', bio_motor, name='bio_motor'),

    path('plane/', plane, name='plane'),
    path('train/', train, name='train'),
    path('bus/', bus, name='bus'),
    path('car/', car, name='car'),
    path('motor/', motor, name='motor'),

    path('process_krt/', process_krt, name='process_krt'),
    path('process_bus/', process_bus, name='process_bus'),


    

    path('', include('theme.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]
