from django.contrib import admin
from .models import Category, Product
from modeltranslation.admin import TranslationAdmin

# Register your models here.


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('name', 'is_active')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ('name', 'price', 'stock', 'is_available', 'created_at')
    list_filter = ('is_available', 'created_at', 'category')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
