from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator, MaxLengthValidator
from decimal import Decimal

# factor para calcular el valor del IVA de acuerdo al tipo
FACTOR_IVA = {
    'standard':0.21,
    'reduced':0.105,
    'zero':0,
}

class Product(models.Model):
    VAT_TYPE_CHOICES = (
    ('standard', '21%'),
    ('reduced', '10,5%'),
    ('zero', 'SIN IVA'),
    )
    sku = models.CharField(max_length=10, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vat_type = models.CharField(max_length=100, choices=VAT_TYPE_CHOICES, default='standard')
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.sku

# Eventualmente voy a querer usar la información de un Customer que ya haya
# ingresado antes.
class Customer(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.IntegerField
    company_name = models.CharField(max_length=30)
    # uso -MinLengthValidator y MaxLengthValidator- para que el código fiscal
    # (CUIT o RUT) tenga exactamente 8 números
    company_tax_id = models.IntegerField(
        validators=[
            MinLengthValidator(8),
            MaxLengthValidator(8)
        ]
    )

class Salesperson(models.Model):
    name = models.CharField(max_length=30)
    
    class Meta:
        app_label = 'pedidos'

# Esta clase representa una orden completa en el sistema
class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    customer = models.CharField(max_length=200)
    salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE)

    def calculate_subtotal(self):
        return sum(line.subtotal for line in self.orderline_set.all())

    @property
    def order_number(self):
        #return a 6 digits long order number
        return f'ORD-{self.id:06d}'
    
    def calculate_taxes(self):
        accumulated_taxes = {
            'standard': Decimal('0.00'), 
            'reduced': Decimal('0.00'), 
            'zero': Decimal('0.00')
            }
        for line in self.orderline_set.all():
            accumulated_taxes[line.vat_type] += line.calculate.iva()
        return accumulated_taxes

    def calculate_total(self):
        return self.calculate_subtotal() + sum(self.calculate_taxes().values())


# Esta clase representa una línea individual de una orden.
class OrderLine(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    vat_type = models.CharField(max_length=100, choices=Product.VAT_TYPE_CHOICES, default='standard')

    def calculate_subtotal(self):
        return self.product.price * self.quantity
    
    def calculate_iva(self):
        iva_para_esta_line = FACTOR_IVA[self.vat_type]
        return self.product.price * iva_para_esta_line

    def save(self, *args, **kwargs):
        self.subtotal = self.calculate_subtotal()
        super().save(*args, **kwargs)
