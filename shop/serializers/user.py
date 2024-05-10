from rest_framework import serializers
from django.contrib.auth import get_user_model
from .cart_item import CartItemSerializer

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, source='cartitem_set', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_admin', 'cart_items']
        extra_kwargs = {'password': {'write_only': True}}