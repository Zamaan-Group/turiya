from django.db import models
from product.models import Product
from user.models import Account


class CardItem(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, related_name='card_item')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

    @property
    def get_total(self):
        return self.product.price * self.quantity


class Order(models.Model):
    STATUS = (
        (1, 'New'),
        (2, 'Process'),
        (3, 'Delivered'),
        (4, 'Canceled'),
    )
    user = models.ForeignKey(Account, models.SET('User deleted'), related_name='order')
    status = models.PositiveIntegerField(choices=STATUS, default=1)
    created_at = models.DateField(auto_now_add=True)
    card_items = models.ManyToManyField(CardItem)

    def __str__(self):
        return self.user.phone

    @property
    def get_total(self):
        items = self.card_items.all()
        return sum([i.get_total for i in items])

    @property
    def get_count(self):
        items = self.card_items.all()
        return sum([i.quantity for i in items])


class Rate(models.Model):
    rate = models.FloatField()
    user = models.ForeignKey(Account, models.SET("User deleted"), related_name='rate')
    product = models.ForeignKey(Product, models.SET('Product deleted'), related_name='rate')

    def __str__(self):
        return self.user.phone


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
