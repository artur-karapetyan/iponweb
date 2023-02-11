from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(upload_to="buyer/", blank=True, null=True)


class Category(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.CharField(max_length=10)


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(upload_to='seller/', blank=True, null=True)


class Stock(models.Model):
    product = models.ManyToManyField(Product)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)


class MyBag(models.Model):
    products = models.ManyToManyField(Product)
