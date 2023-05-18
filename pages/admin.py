from django.contrib import admin
from .models import Category, Product, Service

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug')
    list_display_links = ('pk', 'title')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'category')
    list_display_links = ('pk', 'title')
    list_filter = ('category', )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug')
    list_display_links = ('pk', 'title')
