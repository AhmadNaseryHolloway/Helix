from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path('project/', views.project_view, name="project"),
    path('project/create/', views.project_create_view, name="project_Create"),
    path('project/update/<slug:project_num>', views.project_update_view, name="project_update"),
    path('project/dashboard/<slug:project_num>/', views.project_dashboard_view, name="project_dashboard"),
    path('project/dashboard/project_task/<slug:project_num>/', views.project_task_view, name="project_task"),
    path('project/bom/<slug:project_num>/<str:bom_ty>/', views.bom_dashboard_view, name="bom_dashboard"),
    path('project/dashboard/project_task/create/project_task/<slug:project_num>/', views.project_tasks_create_view, name="project_task_create"),
    path('project/dashboard/project_task/create/task_type/<slug:project_num>/', views.project_tasks_type_create_view, name="project_task_type_create"),
    path('project/dashboard/project_task/create/resource_name/<slug:project_num>/', views.project_resource_create_view, name="project_resource_create"),
]