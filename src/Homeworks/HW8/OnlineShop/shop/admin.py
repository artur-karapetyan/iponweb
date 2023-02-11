from django.contrib import admin
from .models import StoreCategory, ItemCategory, Customer, StoreOwner, Store, Item, MyBag, Purchase


@admin.register(StoreCategory)
class StoreCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'picture']


@admin.register(ItemCategory)
class ItemCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'picture']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'registered_at', 'avatar']


@admin.register(StoreOwner)
class StoreOwnerAdmin(admin.ModelAdmin):
    list_display = ['user', 'registered_at', 'avatar']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['store_category', 'name', 'owner']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'picture', 'category', 'price', 'quantity', 'description', 'store']


class ItemInline(admin.TabularInline):
    model = MyBag.items.through



@admin.register(MyBag)
class MyBagAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_price']
    inlines = [
        ItemInline,
    ]


class PurchaseInLine(admin.TabularInline):
    model = Purchase.items.through


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['buy_time', 'customer', 'total_price']
    inlines = [
        PurchaseInLine,
    ]
