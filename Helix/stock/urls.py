from django.urls import path
from . import views

app_name = 'stock'

urlpatterns = [
    path('stock/', views.stock_list_view, name="stock"),
]