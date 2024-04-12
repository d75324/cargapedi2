from django import forms
from .models import *

class form_cargar_pedidos(forms.ModelForm):
    class Meta:
        model = OrderLine
        fields = ['product',
                  'quantity',
                    ]
