from django.shortcuts import render
from api.models import *
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.template.loader import render_to_string
import json

def order(request):
    cafe = request.GET.get('cafe')
    name = request.GET.get('name')
    items_id = request.GET.get('items-id')
    count = request.GET.get('count')
    price = request.GET.get('price')
    try:
        items_id_list = list(map(int, items_id.split('-')))
        count_list = list(map(int, count.split('-')))
        price_list = list(map(int, price.split('-')))
    except:
        raise Http404('Параметры заказа введены неправильно')

    names_list = [Item.objects.get(id=i).name for i in items_id_list]
    summa = sum([x * y for x, y in zip(count_list,price_list)])



    HttpResponse(cafe)

def menu(request):
    item = list(Item.objects.values('alias', 'price'))

    return JsonResponse({'results':item})