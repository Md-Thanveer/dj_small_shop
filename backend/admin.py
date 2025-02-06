from django.contrib import admin
from .models import Category, Brand, Product, Cart, Order


# Register your models here.

# categroy admin

class CategoryAdmin(admin.ModelAdmin):

    list_display = ('id','name')

    search_fields = ('id','name',)

    ordering = ['id']

admin.site.register(Category,CategoryAdmin)

# brand admin

class BrandAdmin(admin.ModelAdmin):

    list_display = ('id','name','image_path','status',)

    search_fields = ('id','name','status')

    ordering = ['id']

admin.site.register(Brand,BrandAdmin)

# product admin

class ProductAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'image_path','description', 'category', 'brand','price', 'qty','alert_stock',)

    search_fields = ('id', 'name',)

    ordering = ['id']

admin.site.register(Product,ProductAdmin)

# cart admin

class CartAdmin(admin.ModelAdmin):

    list_display = ('id','product','qty',)

    search_fields = ('id','product',)

    ordering = ['id']

admin.site.register(Cart,CartAdmin)

# order admin

class OrderAdmin(admin.ModelAdmin):

    list_display = ('id', 'order_number', 'order_date', 'total_amount', 'order_status', 'payment_method',)

    search_fields = ('id', 'order_number','order_status','payment_method')

    ordering = ['id']

admin.site.register(Order, OrderAdmin)