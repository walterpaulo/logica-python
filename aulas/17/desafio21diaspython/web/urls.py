from django.contrib import admin
from django.urls import include, path

from . import views
from .controllers import home_controller, cliente_controller

urlpatterns = [
    path('', home_controller.index),
    path('clientes', cliente_controller.index)
    # path('tamplate', views.tamplate),
    # path('html_bruto', views.html_bruto),
    # path('json', views.json),
]
