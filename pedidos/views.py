from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def form_carga_productos(request):
    return render(request, 'carga.html')

def form_pedidos(request):
    return render(request, 'pedidos.html')
