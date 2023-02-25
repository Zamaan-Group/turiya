from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='categories')

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, models.CASCADE, related_name='subcategory')

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    new_price = models.PositiveIntegerField(null=True, blank=True)
    is_delivery = models.BooleanField(default=False)
    price_delivery = models.PositiveIntegerField(null=True, blank=True)
    phone = models.BooleanField(default=False)
    type_cash = models.CharField(max_length=255)
    return_day = models.PositiveIntegerField()
    category = models.ForeignKey(Subcategory, models.SET_NULL, null=True)
    brand = models.CharField(max_length=255)
    made_in = models.CharField(max_length=255)
    color = models.ForeignKey(Color, models.SET_NULL, null=True)
    description = models.TextField()
    characteristic = models.CharField(max_length=255)
    rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def get_rating(self):
        user_count = self.rate.all().count()
        if user_count == 0:
            user_count = 1
        rate_summa = sum([item.rate for item in self.rate.all()])
        self.rating = rate_summa / user_count
        self.save()
        return self.rating

    class Meta:
        ordering = ['rating']


class ProductImage(models.Model):
    product = models.ForeignKey(Product, models.CASCADE, related_name='product_image')
    image = models.ImageField(upload_to='product_images')
