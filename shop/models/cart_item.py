from django.db import models
from .user import User
from .product import Product

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def save(self, *args, **kwargs):
        existing_cart_item = CartItem.objects.filter(user=self.user, product=self.product).first()
        if existing_cart_item and existing_cart_item.pk != self.pk:
            existing_cart_item.quantity = self.quantity
            existing_cart_item.save()
        else:
            super().save(*args, **kwargs)