from django.shortcuts import render
from api.models import *
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.template.loader import render_to_string
import json

def order(request):
    if request.method != "POST":
        waiter_id = request.GET.get('waiter-id')
        item_ids = request.GET.get('item-ids')
        item_counts = request.GET.get('item-counts')
        item_prices = request.GET.get('item-prices')
        try:
            item_ids_list = list(map(int, item_ids.split('-')))
            count_list = list(map(int, item_counts.split('-')))
            item_prices_list = list(map(int, item_prices.split('-')))
        except:
            raise Http404('Параметры заказа введены неправильно')

        order_total = sum([x * y for x, y in zip(count_list,item_prices_list)])

        newOrder = Order()
        newOrder.waiter = Waiters.objects.get(id=waiter_id)
        newOrder.order_place = Waiters.objects.get(id=waiter_id).work_place
        newOrder.save()

        for i in range(len(item_ids_list)):
            orderLine = OrderLine()
            orderLine.order = newOrder
            orderLine.item = Item.objects.get(id= item_ids_list[i])
            orderLine.count = count_list[i]
            orderLine.item_price = item_prices_list[i]
            orderLine.save()

def menu(request):
    item = list(Item.objects.values())
    return JsonResponse({'results':item})
