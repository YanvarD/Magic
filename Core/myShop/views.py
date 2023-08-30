from django.shortcuts import render, HttpResponse
from .models import *


menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': "Категории", 'url_name': 'category'},
    {'title': "Ремонт", 'url_name': 'repair'},
    {'title': "Железо", 'url_name': 'product'},
    {'title': "Войти", 'url_name':'login'},
]

def mainWindow(request):
    category = Category.objects.all()
    context={'category':category, 
             'menu': menu, 
            'title': 'Главная станица'}
    return render(request, 'myShop/mainWindow.html', context=context)

def about(request):
    context={'menu': menu, 
            'title': 'О нас'}
    return render(request, 'myShop/aboutUs.html', context=context)
    
def cat(request):
    context= {'menu': menu, 
            'title': 'Категории'}
    return render(request, 'myShop/сat.html', context=context)

def repair(request):
    category = Category.objects.all()
    context={'category':category, 
             'menu': menu, 
            'title': 'Главная станица'}
    return render(request, 'myShop/remont.html', context=context)

def product(request):
    product = Product.objects.all()
    context= {'product': product, 'title': 'Железо', 'menu':menu}
    return render(request, 'myShop/product_base.html', context=context)

def login(request):
    context={'menu': menu, 
            'title': 'Категории'}
    return render(request, 'myShop/login.html', context=context)

    
