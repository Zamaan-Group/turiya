from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='categories')


class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, models.CASCADE, related_name='subcategory')


class Color(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    new_price = models.PositiveIntegerField()
    is_delivery = models.BooleanField(default=False)
    price_delivery = models.PositiveIntegerField()
    phone = models.BooleanField(default=False)
    type_cash = models.CharField(max_length=255)
    return_day = models.DateField()
    category = models.ForeignKey(Subcategory, models.SET_NULL, null=True)
    brand = models.CharField(max_length=255)
    made_in = models.CharField(max_length=255)
    color = models.ForeignKey(Color, models.SET_NULL, null=True)
    description = models.TextField()
    characteristic = models.CharField(max_length=255)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, related_name='product_image')
    image = models.ImageField(upload_to='product_images')


