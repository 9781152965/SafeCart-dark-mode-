from django.contrib import admin
from .models import Product, Contact, Order, OrderUpdate,   Customer, Category ,Product2 ,Cart , CartProduct ,Order2 


class AdminProduct(admin.ModelAdmin):
    list_display = ['product_id','product_name', 'category','price']

class AdminOrderUpdate(admin.ModelAdmin):
    list_display = ['order_id' , 'timestamp']

class AdminOrder(admin.ModelAdmin):
    list_display = ['name', 'order_id', 'address',]


# Register your models here.

admin.site.register(Product , AdminProduct)
admin.site.register(Contact)
admin.site.register( Customer)
admin.site.register( Category)
admin.site.register( Product2)
admin.site.register( Cart)
admin.site.register( CartProduct)
admin.site.register( Order2)
admin.site.register(Order , AdminOrder)
admin.site.register(OrderUpdate , AdminOrderUpdate)