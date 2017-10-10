from django.contrib import admin
from api.models import *

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price') # какие свойства Item должны показываться в админке

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

# class SubcategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')

class ZakazAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'data')

admin.site.register(Item, ItemAdmin) # чтобы модель Item стала доступна на стр админки
admin.site.register(Category, CategoryAdmin)
admin.site.register(Zakaz, ZakazAdmin)
#admin.site.register(Subcategory, SubcategoryAdmin)

