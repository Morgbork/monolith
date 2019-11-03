from django.db import models
from django.urls import reverse


class Goods(models.Model):
    product_code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.SlugField(max_length=150, blank=True)
    manufacturer = models.SlugField(max_length=50)
    stock = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True)

    class Meta:
        ordering = ['product_code']
        verbose_name_plural = 'Goods'

    def __str__(self):
        return self.name
