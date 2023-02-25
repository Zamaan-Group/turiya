from rest_framework import serializers
from .models import Order, CardItem


class CardItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardItem
        fields = ['id', 'product', 'quantity', 'product_name', 'get_total']

    product_name = serializers.CharField(source='product.name', read_only=True)
    get_total = serializers.IntegerField(read_only=True)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['user', 'status', "card_items"]

    # card_items = CardItemSerializer(many=True, write_only=True)


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status', 'get_total', 'created_at', 'get_count', 'card_items']

    card_items = CardItemSerializer(many=True, read_only=True)
    status = serializers.CharField(source='get_status_display')
