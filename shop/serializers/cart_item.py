from rest_framework import serializers
from ..models import CartItem
from .product import ProductSerializer

class CartItemSerializer(serializers.ModelSerializer):
    Product = ProductSerializer(read_only=True, source='product')

    class Meta:
        model = CartItem
        fields = ['id', 'user', 'product', 'Product', 'quantity']