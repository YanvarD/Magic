from django.urls import path
from myShop.views import *
urlpatterns = [
    path('', mainWindow, name='home'),
    path('about/', about, name='about'),
    path('category/', cat, name='category'),
    path('product/', product, name='product'),
    path('repair/', repair, name='repair'),
    path('login/', login, name='login'),
    
    
]
