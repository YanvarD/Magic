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
    return render(request, 'myShop/aboutUs.html', {'menu': menu, 
                                                      'title': 'О нас'})
    
def cat(request):
    return HttpResponse('category')

def repair(request):
    return HttpResponse('repair')

def product(request):
    return HttpResponse('product')

def login(request):
    return HttpResponse('login')

    
