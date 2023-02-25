from rest_framework import serializers
from .models import Product, Category, Subcategory, ProductImage


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'icon', 'subcategory']

    subcategory = SubcategorySerializer(many=True)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'get_rating', 'product_image', 'description']

    product_image = ProductImageSerializer(many=True, read_only=True)


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'price', 'is_delivery', 'price_delivery', 'new_price', 'made_in', 'brand', 'color',
                  'return_day', 'type_cash', 'description', 'category', 'product_image']

    product_image = ProductImageSerializer(many=True)
