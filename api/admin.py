from django.contrib import admin
from api.models import *

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'item_name', 'price') # какие свойства Item должны показываться в админке

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_place', 'waiter', 'date', 'order_total', 'payment')
    list_editable = ('payment',)

class OrderLineAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'order', 'count', 'item_price')

class WaitersAdmin(admin.ModelAdmin):
    list_display = ('id', 'waiter_name', 'work_place')

class OrderPlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'place_name')


admin.site.register(Item, ItemAdmin) # чтобы модель Item стала доступна на стр админки
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine, OrderLineAdmin)
admin.site.register(Waiters, WaitersAdmin)
admin.site.register(OrderPlace, OrderPlaceAdmin)

