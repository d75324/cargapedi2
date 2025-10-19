from django.urls import path
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from .forms import CustomLoginForm

urlpatterns = [
    path('', views.home, name='home'),
    path('carga/', views.view_cargar_pedidos, name='carga'),
    path('pedidos/', views.form_pedidos, name='pedidos'),
    path('salesperson/', views.salesperson_view, name='salesperson'),
    path('rustico/', views.rustico_view, name='rustico'),
    path('admin/login/', auth_views.LoginView.as_view(form_class=CustomLoginForm)),
    #path('admin/', admin.site.urls),
]