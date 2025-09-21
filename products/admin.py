from django.contrib import admin

from django_jalali.admin.filters import JDateFieldListFilter

import django_jalali.admin as jadmin

from .models import Product, Comment


class CommentsInLine(admin.TabularInline):
    model = Comment
    fields = ['author','text','stars','active',]
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','description','active','datetime_modified',]
    inlines = [
        CommentsInLine,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author','product','text','stars','active','datetime_modified',]

