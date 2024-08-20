from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from core.erp.models import *
# Create your views here.

def myfirstview(request):
    data ={
        'name' : 'william',
        'categories': Category.objects.all(),
        # 'products': Product.objects.all()
    }
    # return HttpResponse('hola esta es mi primera URL')
    return render(request, 'index.html', data)

def mysecondview(request):
    data ={
        'name' : 'william',
        'categories': Category.objects.all(),
        'products': Product.objects.all()
    }
    return render(request, 'second.html', data)