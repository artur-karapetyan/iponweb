from django.contrib import admin
from django.urls import path
from .api.StoreCategory import StoreCategoryView

urlpatterns = [
    path('StoreCategory/', StoreCategoryView.as_view()),
    path('StoreCategory/<int:id>', StoreCategoryView.check_view)
]