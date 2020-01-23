from django.contrib import admin
from . import models


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_time',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'order_date',)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'invoice', 'amount', 'transaction_date', 'status')


class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'order',)


admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderItem, OrderItemAdmin)
admin.site.register(models.Invoice, InvoiceAdmin)
admin.site.register(models.Transaction, TransactionAdmin)


