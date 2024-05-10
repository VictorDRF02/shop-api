from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..serializers import CartItemSerializer
from ..models import CartItem

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]
