from django.shortcuts import render


def defaultpage(request):
    return render(request, 'myShop/default.html')
    
