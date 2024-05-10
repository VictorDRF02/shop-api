from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'cartItems', views.CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]