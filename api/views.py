from django.shortcuts import render
from api.models import *
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.template.loader import render_to_string
import json
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("OK")
        else:
            raise Http404('Uncorrect name or password')

def order(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            waiter_id = request.POST.get('waiter-id')
            item_ids = request.POST.get('item-ids')
            item_counts = request.POST.get('item-counts')
            #item_prices = request.POST.get('item-prices')
            try:
                item_ids_list = list(map(int, item_ids.split('-')))
                count_list = list(map(int, item_counts.split('-')))
                #item_prices_list = list(map(int, item_prices.split('-')))
            except:
                raise Http404('Параметры заказа введены неправильно')

            item_prices_list = []
            for i in range(len(item_ids_list)):
                item_prices_list.append(Item.objects.get(id= item_ids_list[i]).price)

            order_total = sum([x * y for x, y in zip(count_list,item_prices_list)])

            newOrder = Order()
            newOrder.waiter = Waiters.objects.get(id=waiter_id)
            newOrder.order_place = Waiters.objects.get(id=waiter_id).work_place
            newOrder.order_total = order_total
            newOrder.save()

            for i in range(len(item_ids_list)):
                orderLine = OrderLine()
                orderLine.order = newOrder
                orderLine.item = Item.objects.get(id= item_ids_list[i])
                orderLine.count = count_list[i]
                orderLine.item_price = item_prices_list[i]
                orderLine.save()
            return HttpResponse('Ok')
        else:
            raise Http404('It is necessary to login')
    else:
        raise Http404('Not a post request')

def menu(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            item = list(Item.objects.values())
            return JsonResponse({'results':item})
