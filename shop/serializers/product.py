from rest_framework import serializers
from ..models import Category, Product
from .review import ReviewSerializer

class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    Categories = CategoryProductSerializer(read_only=True, many=True, source='categories')
    reviews = ReviewSerializer(many=True, source='review_set', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'categories', 'Categories', 'reviews']