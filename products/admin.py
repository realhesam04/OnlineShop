from django.contrib import admin

from .models import Product, Comment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','description','active','datetime_modified',]


@admin.register(Comment)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['author','product','text','stars','active','datetime_modified',]