from django.shortcuts import render
from .models import StockItems
# Create your views here.

def stock_list_view(request, *args, **kwargs):
    stock_list = StockItems.objects.all()
    return render(request, "stock/stock_list.html", {'stock_list' : stock_list})