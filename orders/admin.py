from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['book']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'shipping_address',  'order_completed', 'created',
                    'updated']
    list_filter = ['order_completed', 'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
# Register your models here.
