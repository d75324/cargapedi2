from django.views.generic import TemplateView
from .models import Product
from django.shortcuts import render
from .forms import *

def home(request):
    return render(request, 'home.html')

def view_cargar_pedidos(request):
    context = {}
    if request.method == 'POST':
        producto_ordenado = view_cargar_pedidos(request.POST)
        if producto_ordenado.is_valid():
            view_cargar_pedidos = producto_ordenado.save()
            context['view_cargar_pedidos'] = view_cargar_pedidos
            producto_ordenado = view_cargar_pedidos()
    else:
        producto_ordenado = view_cargar_pedidos()
    context ['producto_ordenado'] = producto_ordenado
    return render(request, 'carga.html', context)


def form_pedidos(request):
    return render(request, 'pedidos.html')

# Para mostrar el valor del SKU directamente desde el modelo Product en el template, voy a pasar una instancia de Product desde la vista al template:

def productos(request, id):
    productos = Product.objects.get(id=id)
    context = {'productos': productos}
    return render(request, 'pedidos.html', context)

def salesperson_view(request):
    salespersons = Salesperson.objects.all()
    context = {'salespersons': salespersons}
    return render(request, 'salesperson.html', context)