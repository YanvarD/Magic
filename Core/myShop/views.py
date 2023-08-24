from django.shortcuts import render
from .models import *


menu = ["О сайте", "Категории", "Ремонт", "О нас"]

def mainWindow(request):
    category = Category.objects.all()
    return render(request, 'myShop/mainWindow.html', {'category':category, 'menu': menu, 
                                                      'title': 'Главная станица'})

def about(request):
    return render(request, 'myShop/aboutUs.html', {'menu': menu, 
                                                      'title': 'О нас'})
    
