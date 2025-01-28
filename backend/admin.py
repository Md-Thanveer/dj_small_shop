from django.contrib import admin
from .models import Category
from .models import Brand

#register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'name',)
    search_fields = ('name',)
    ordering = ['id']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)
    ordering = ['id']
