from django.shortcuts import render
from api.models import *
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.template.loader import render_to_string
import json

def order(request):
    pass
    # cafe = request.GET.get('cafe')
    # name = request.GET.get('name')
    # item_ids = request.GET.get('item_ids')
    # item_counts = request.GET.get('item_counts')
    # item_prices = request.GET.get('item_prices')
    # try:
    #     items_id_list = list(map(int, item_ids.split('-')))
    #     count_list = list(map(int, item_counts.split('-')))
    #     price_list = list(map(int, item_prices.split('-')))
    # except:
    #     raise Http404('Параметры заказа введены неправильно')
    #
    # names_list = [Item.objects.get(id=i).name for i in items_id_list]
    # order_total = sum([x * y for x, y in zip(count_list,price_list)])
    #
    # newOrder = Order()
    # newOrder.name = name
    # newOrder.save()
    #
    # for index in items_id_list
    #     item_id = items_id_list[index]
    #     price = price_list[index]
    #     count = count_list[index]
    #     orderLine = OrderLine()
    #     orderLine.order = newOrder
    #     orderLine.item = Item.objects.get(id = item_id)
    #     orderLine.count = ...
    #     orderLine.save()

def menu(request):
    item = list(Item.objects.values('alias', 'price'))
    return JsonResponse({'results':item})
