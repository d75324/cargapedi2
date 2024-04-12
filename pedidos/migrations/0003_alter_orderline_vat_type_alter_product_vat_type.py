# Generated by Django 5.0.4 on 2024-04-12 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_rename_customer_email_customer_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderline',
            name='vat_type',
            field=models.CharField(choices=[('standard', '21%'), ('reduced', '10,5%'), ('zero', 'SIN IVA')], default='standard', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='vat_type',
            field=models.CharField(choices=[('standard', '21%'), ('reduced', '10,5%'), ('zero', 'SIN IVA')], default='standard', max_length=100),
        ),
    ]
