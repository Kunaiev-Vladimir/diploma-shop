from django.contrib import admin
from .models import Language

# Register your models here.


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'flag', 'is_active', 'sort')
    list_editable = ('is_active', 'sort')
    search_fields = ('name', 'code')
