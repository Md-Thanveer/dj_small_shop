from django.contrib import admin
from django.utils.html import format_html
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
    list_display = ('id', 'name', 'image_tag')
    search_fields = ('name',)
    ordering = ['-id']

    def image_tag(self, obj):
        return format_html('<img src = "{}" width = "150" height="150" />'.format(obj.image_path.url))

    image_tag.short_description = 'Image'

