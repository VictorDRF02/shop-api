from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from ..permissions import IsAdminOrReadOnly
from ..serializers import ProductSerializer
from ..models import Product
from django.db.models import Q

class Pagination(PageNumberPagination):
    page_size = 16
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]
    pagination_class = Pagination

    def get_queryset(self):
        queryset = Product.objects.all()
        search = self.request.query_params.get('search', None)
        price = self.request.query_params.get('price', None)
        category = self.request.query_params.get('category', None)
        order = self.request.query_params.get('order', None)

        if search is not None or search is '':
            queryset = queryset.filter(Q(name__icontains=search) | Q(description__icontains=search))
        if price is not None and len(price.split(':')) == 2:
            price = price.split(':')
            queryset = queryset.filter(Q(price__gte=price[0]), Q(price__lte=price[1]))
        if category:
            queryset = queryset.filter(Q(categories__id__exact=category))
        if order is not None:
            queryset = queryset.order_by(order)
    
        return queryset