from django.shortcuts import render
from api.models import *
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.template.loader import render_to_string
import json


def menu(request):
    item = list(Item.objects.values('alias', 'price'))

    return JsonResponse({'results':item})