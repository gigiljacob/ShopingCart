from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import User

class ProductCategory(models.Model):
    category_name = models.CharField(max_length=40, null=False, blank=False)
    description = models.TextField(max_length=155, null=True, blank=True)
    show = models.BooleanField(default=True, null=False, blank=False)

    def __str__(self):
        return self.category_name


class Review(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=50, null=False, blank=False)
    descritpion = models.TextField(max_length=255, null=True, blank=True)
    rating = models.PositiveIntegerField(null=False, blank=False)
    images = models.ImageField(upload_to='review/product/', null=True, blank=True)
    like = models.PositiveIntegerField(null=True, blank=True, default=0)
    dis_like = models.PositiveIntegerField(null=True, blank=True, default=0)

    def __str__(self):
        return self.heading


class Product(models.Model):
    name = models.CharField(max_length=155, null=False, blank=False)
    images = models.ImageField(upload_to='product/', null=True, blank=True)
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)
    descritpion = models.TextField(max_length=255, null=False, blank=False)
    mrp = models.PositiveIntegerField(null=False, blank=False)
    discount = models.FloatField(null=False, blank=False)
    price = models.PositiveIntegerField(null=False, blank=False)
    review = models.ForeignKey(to=Review, on_delete=models.CASCADE, null=True, blank=True)
    in_stock = models.BooleanField(null=False, blank=False, default=True)
    inventory = models.PositiveIntegerField(null=False, blank=False, default=1)
    created_at = models.DateTimeField(auto_created=True, null=False, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=False)
    slug = models.SlugField(null=False, blank=False, default=name)

    def __str__(self):
        return self.name


@receiver(post_save, sender=Product)
def product_slug_generate(sender, instance, **kwargs):
    print(instance)
