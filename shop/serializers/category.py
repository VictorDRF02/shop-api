from rest_framework import serializers
from ..models import Category
from .product import ProductSerializer

class CategorySerializer(serializers.ModelSerializer):
    Products = ProductSerializer(read_only=True, many=True, source='products')

    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'image', 'products', 'Products']

