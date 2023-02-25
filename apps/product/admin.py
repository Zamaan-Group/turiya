from django.contrib import admin
from .models import Category, Subcategory, Product, ProductImage, Color


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Color)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Subcategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id']


@admin.register(ProductImage)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id']
