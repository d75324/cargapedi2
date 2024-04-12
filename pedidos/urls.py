from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('carga/', views.view_cargar_pedidos, name='carga'),
    path('pedidos/', views.form_pedidos, name='pedidos'),
]