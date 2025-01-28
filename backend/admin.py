from django.contrib import admin
from .models import Category
from .models import Brand

#register your models here.
admin.site.register(Category)

admin.site.register(Brand)
