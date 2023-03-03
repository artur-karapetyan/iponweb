from django.contrib import admin

#
from .models import StoreCategory, ItemCategory, Customer, StoreOwner, Store, Item, MyBag, Purchase, UserAuth

# Change Header
admin.site.site_header = "Online Shop"


@admin.register(UserAuth)
class UserAuthAdmin(admin.ModelAdmin):
    list_display = ("user_info", 'verification_code')
    search_fields = ("user__first_name", "user__last_name")

    #
    def user_info(self, obj):
        return "{}".format(
            " ".join([obj.user.first_name, obj.user.last_name])
        )

    user_info.short_description = "Generic user"


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
