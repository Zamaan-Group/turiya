from django.db import models
from product.models import Product
from user.models import User


class Order(models.Model):
    STATUS = (
        (1, 'New'),
        (2, 'Process'),
        (3, 'Delivered'),
        (4, 'Canceled'),
    )
    product = models.ForeignKey(Product, models.SET('Product deleted'), related_name='order')
    user = models.ForeignKey(User, models.SET('User deleted'), related_name='order')
    count = models.PositiveIntegerField(default=1)
    status = models.PositiveIntegerField(choices=STATUS, default=1)
    created_at = models.DateTimeField(auto_now_add=True)


class Rate(models.Model):
    rate = models.FloatField()
    user = models.ForeignKey(User, models.SET("User deleted"), related_name='rate')
    product = models.ForeignKey(Product, models.SET('Product deleted'), related_name='rate')


class Slider(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='sliders')
    title = models.CharField(max_length=255)


class Campaign(models.Model):
    class Meta:
        verbose_name = 'Aksiya'
        verbose_name_plural = 'Aksiyalar'
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='campaign')
