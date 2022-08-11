from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index),
    path('tamplate', views.tamplate),
    path('html_bruto', views.html_bruto),
    path('json', views.json),
]