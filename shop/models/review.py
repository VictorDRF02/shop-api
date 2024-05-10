from django.db import models
from .user import User
from .product import Product

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()
    
    def save(self, *args, **kwargs):
        existing_review = Review.objects.filter(user=self.user, product=self.product).first()
        if existing_review and existing_review.pk != self.pk:
            existing_review.rating = self.rating
            existing_review.comment = self.comment
            existing_review.save()
        else:
            super().save(*args, **kwargs)