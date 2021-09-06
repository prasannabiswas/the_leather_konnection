from django.shortcuts import render
from .models import Bag

def home(request):
    return render(request, 'products/home.html')

def bag(request):
    bags = Bag.objects.all()
    return render(request, 'products/bags.html', {'bags':bags})

def wallet(request):
    return render(request, 'products/wallets.html')