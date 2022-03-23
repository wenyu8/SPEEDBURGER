from django.contrib import admin
from .models import User, Product, OrderDetail, Order, Email

class UserList(admin.ModelAdmin):
    list_display = ( 'firstName', 'lastName', 'email' )
    list_filter = ( 'firstName', 'lastName', 'email')
    search_fields = ('email', )
    ordering = ['userId']


class ProductList(admin.ModelAdmin):
    list_display = ( 'productName', 'price', 'calories' )
    list_filter = ( 'productName',)
    search_fields = ('productName', 'description')
    ordering = ['productName']


class OrderDetailList(admin.ModelAdmin):
    list_display = ( 'firstName', 'productID', 'quantity', 'order_timestamp', 'amount' )
    list_filter = ( 'status', 'firstName')
    search_fields = ('firstName', )
    ordering = ['order_timestamp']


class OrderList(admin.ModelAdmin):
    list_display = ( 'email', 'orderTotal', 'status' )
    list_filter = ( 'email', 'status')
    search_fields = ('email', )
    ordering = ['status']


class EmailList(admin.ModelAdmin):
    list_display = ( 'email', )
    list_filter = ( 'email', )
    search_fields = ('email', )
    ordering = ['email']

admin.site.register(User, UserList)
admin.site.register(Product, ProductList)
admin.site.register(OrderDetail, OrderDetailList)
admin.site.register(Order, OrderList)
admin.site.register(Email, EmailList)
