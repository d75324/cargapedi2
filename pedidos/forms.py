from django import forms
from .models import Salesperson, OrderLine
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class form_cargar_pedidos(forms.ModelForm):
    class Meta:
        model = OrderLine
        fields = ['product',
                  'quantity',
                    ]

class SalespersonForm(forms.Form):
    salesperson_choices = [(sp.id, sp.name) for sp in Salesperson.objects.all()]
    salesperson = forms.ChoiceField(choices=salesperson_choices, widget=forms.Select)

class SalespersonForm2(forms.Form):
    salesperson_choices = [(sp.id, sp.name) for sp in Salesperson.objects.all()]
    salesperson = forms.ChoiceField(choices=salesperson_choices, widget=forms.Select)


class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = 'admin:login'  # Ajusta la acción del formulario si es necesario
        self.helper.add_input(Submit('submit', 'Log in'))