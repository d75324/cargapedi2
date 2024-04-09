from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator, MaxLengthValidator
from decimal import Decimal


class Product(models.Model):
    sku = models.CharField(max_length=10, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    VAT_TYPE_CHOICES = (
        ('standard', 'Standard (21%)'),
        ('reduced', 'Reducido (10,5%)'),
        ('zero', 'SIN IVA'),
    )
    vat_type = models.CharField(max_length=100, choices=VAT_TYPE_CHOICES, default='standard')
    description = models.CharField(max_length=100)


# Eventualmente voy a querer usar la información de un Customer que ya haya
# ingresado antes.
class Customer(models.Model):
    customer_name = models.CharField(max_length=30)
    customer_lastname = models.CharField(max_length=30)
    customer_email = models.EmailField()
    customer_phonenumber = models.IntegerField
    company_name = models.CharField(max_length=30)
    # uso -MinLengthValidator y MaxLengthValidator- para que el código fiscal
    # (CUIT o RUT) tenga exactamente 8 números
    company_tax_id = models.IntegerField(
        validators=[
            MinLengthValidator(8),
            MaxLengthValidator(8)
        ]
    )

# Esta clase representa una orden completa en el sistema
class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    customer = models.CharField(max_length=200)
    def calculate_subtotal(self):
        return sum(line.subtotal for line in self.orderline_set.all())

    def calculate_taxes(self):
        tax_rates = {'standard': Decimal('0.21'), 'reduced': Decimal('0.105'), 'zero': Decimal('0.00')}
        return sum(line.product.price * tax_rates[line.product.vat_type] for line in self.orderline_set.all())

    def calculate_total(self):
        return self.calculate_subtotal() + self.calculate_taxes()

# factor para calcular el valor del IVA de acuerdo al tipo
FACTOR_IVA = {
    'standard':1.21,
    'reduced':1.105,
    'zero':1,
}


# Esta clase representa una línea individual de una orden.
class OrderLine(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def calculate_subtotal(self):
        return self.product.price * self.quantity
    
    def calculate_iva(self):
        iva_para_este_producto = FACTOR_IVA[self.vat_type]
        return self.product.price * iva_para_este_producto

    def save(self, *args, **kwargs):
        self.subtotal = self.calculate_subtotal()
        super().save(*args, **kwargs)
