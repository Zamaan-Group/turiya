# Generated by Django 3.2.18 on 2023-02-25 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='new_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_delivery',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
