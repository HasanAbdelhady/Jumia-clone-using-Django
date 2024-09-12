from django.db import models
from django.shortcuts import  reverse
from category.models import Category

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=500, null=True, blank=True)
    image=  models.ImageField(upload_to='products/images/', null=True, blank=True)
    rating = models.FloatField(default=0)
    in_stock = models.BooleanField(blank=False)
    category = models.ForeignKey(Category, null=True, blank=True , on_delete=models.CASCADE,
                              related_name='products')


    # level of the application
    def __str__(self):
        return self.name
    
    @property
    def image_url(self):
        return f'/media/{self.image}'
    
    @property
    def show_url(self): # self.id
        url = reverse("one_product.index", args=[self.id])
        return url
