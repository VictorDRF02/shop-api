from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/products/', null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name='products', blank=True)
    
    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        # TODO Agregar la categoría `Todos los productos` (id=1) como predeterminada.
        super(Product, self).save(*args, **kwargs)
    