from django.views.generic import TemplateView
from .models import Product, Salesperson
from django.shortcuts import render
from .forms import SalespersonForm, SalespersonForm2

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

# en lugar de form le pongo arnold de nombre y uso este nombre (arnold) para
# llamarla desde el template:

def salesperson_view(request):
    if request.method == 'POST':
        arnold = SalespersonForm(request.POST)
        if arnold.is_valid():
            selected_salesperson_id = arnold.cleaned_data['salesperson']
    else:
        arnold = SalespersonForm()

    context = {'arnold': arnold}
    return render(request, 'salesperson.html', context)

def rustico_view(request):
    if request.method == 'POST':
        romualdo = SalespersonForm2(request.POST)
        if romualdo.is_valid():
            selected_salesperson_id = romualdo.cleaned_data['salesperson']
        else:
            romualdo = SalespersonForm2()

    context = {'romualdo': romualdo}
    return render(request, 'rustico.html', context)