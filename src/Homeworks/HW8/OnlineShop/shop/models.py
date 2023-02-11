from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import admin


class StoreCategory(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="StoreCategory/", blank=True, null=True)


class ItemCategory(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="ItemCategory/", blank=True, null=True)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(upload_to="customer/", blank=True, null=True)


class StoreOwner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(default=timezone.now)
    avatar = models.ImageField(upload_to='StoreOwner/', blank=True, null=True)


class Store(models.Model):
    store_category = models.ForeignKey(StoreCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(StoreOwner, on_delete=models.CASCADE)


class Item(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="Items/", blank=True, null=True)
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.FloatField()
    description = models.CharField(max_length=500)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)


class MyBag(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    total_price = models.FloatField()


class Purchase(models.Model):
    items = models.ManyToManyField(Item)
    buy_time = models.DateTimeField(default=timezone.now)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.FloatField()
