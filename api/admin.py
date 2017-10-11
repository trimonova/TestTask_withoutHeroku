from django.contrib import admin
from api.models import *

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price') # какие свойства Item должны показываться в админке

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date')

class OrderLineAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'order', 'count')


admin.site.register(Item, ItemAdmin) # чтобы модель Item стала доступна на стр админки
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine, OrderLineAdmin)

