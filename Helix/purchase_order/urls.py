from django.urls import path
from . import views

app_name = 'po'

urlpatterns = [
    path('purchaseorder/dashboard/<slug:project_num>/<order_number>/', views.purchase_order_dashboard_view, name="PODashboard"),
    path('purchaseorder/create/<slug:project_num>-<counter>/', views.purchase_order_create, name="POCreate")
]