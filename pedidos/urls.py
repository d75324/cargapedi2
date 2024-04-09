from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('carga/', views.form_carga_productos, name='carga'),
    path('pedidos/', views.form_pedidos, name='pedidos'),
]