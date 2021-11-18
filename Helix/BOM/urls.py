from django.urls import path
from . import views

app_name = 'bom'

urlpatterns = [
    path('project/bom/create/bom/<slug:project_num>/<str:bom_type>', views.bom_create_view, name='bom_create'),
    path('project/bom/create/bomtype/<slug:project_num>', views.bom_type_create_view, name='bomtype_create'),
    path('project/bom/update/bomtype/<slug:project_num>/<str:bom_type>', views.bom_type_update_view, name='bomtype_update'),
]