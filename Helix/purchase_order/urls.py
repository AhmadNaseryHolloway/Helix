from django.urls import path
from . import views

app_name = 'po'

urlpatterns = [
    path('purchaseorder/dashboard/<slug:project_num>/<order_number>/', views.purchase_order_dashboard_view, name="PODashboard"),
    path('purchaseorder/create/<slug:project_num>-<counter>/', views.purchase_order_create, name="POCreate"),
    path('purchaseorder/update/<slug:project_num>/<str:order_number>/', views.purchase_order_update, name="POUpdate"),

    path('purchaseorder/PoLine/create/<slug:project_num>/<order_number>/', views.purchase_order_po_line_create, name="POLineItemCreate"),

    path('purchaseorder/view_pdf/<slug:order>/', views.purchase_order_view_PDF_view, name="POPDF"),
]