from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from ..permissions import IsAdminOrReadOnly
from ..serializers import CategorySerializer
from ..models import Category
from django.db.models import Q

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def get_queryset(self):
        queryset = Category.objects.all()
        search = self.request.query_params.get('search', None)
        price = self.request.query_params.get('price', None)
        order = self.request.query_params.get('order', None)
        if search is not None:
            queryset = queryset.filter(Q(name__icontains=search) | Q(description__icontains=search) | Q(products__name__icontains=search))
        if price is not None and len(price.split(':')) == 2:
            price = price.split(':')
            queryset = queryset.filter(Q(products__price__gte=price[0]), Q(products__price__lte=price[1]))
        if order:
            queryset = queryset.order_by(order)
        return queryset