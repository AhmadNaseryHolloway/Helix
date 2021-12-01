from django.shortcuts import redirect, render
from .filters import ProjectFilter
from Helix.utlis import render_to_pdf
from django.http.response import HttpResponse

from purchase_order.models import PurchaseOrder

from .models import Project, ProjectTasks, Stage
from BOM.models import BOM, BOMType, SubSection

from .forms import ProjectCreateForm, ProjectUpdateForm, ProjectTasksCreateForm, TasksTypeCreateForm, ResourceCreateForm

# Create your views here.

def project_view(request, *args, **kwargs):
    project_list = Project.objects.all()

    myFilter = ProjectFilter(request.GET, queryset=project_list)
    project_list = myFilter.qs
    context = {
        'project_list' : project_list,
        'myFilter': myFilter,
    }
    return render(request, "project/project_view.html", context)

def bom_dashboard_view(request, project_num, bom_ty, *args, **kwargs):
    project_info = Project.objects.filter(project_Number=project_num)
    BOM_info = BOM.objects.filter(project_Number=project_num, bom_type=bom_ty).order_by('sub_Section')
    BOM_type = BOMType.objects.filter(project_Number=project_num)
    sub_sec = SubSection.objects.filter(bom__bom_type__bom_Type=bom_ty).distinct()

    context = {
        "project_info" : project_info,
        "bom_info": BOM_info,
        "bom_type_list": BOM_type,
        "bom_ty": bom_ty,
        "sub_sec": sub_sec,
        "project": project_num
        }

    return render(request, "bom/bom_dashboard_view.html", context)

def project_dashboard_view(request, project_num, *args, **kwargs):
    project_info = Project.objects.filter(project_Number=project_num)

    stage = Stage.objects.filter(projecttasks__project_Number=project_num).distinct().order_by('stage_Order')
    proj_task = ProjectTasks.objects.filter(project_Number=project_num)

    BOM_info = BOM.objects.filter(project_Number=project_num)
    BOM_type = BOMType.objects.filter(project_Number=project_num)

    purchase_order = PurchaseOrder.objects.filter(project_Number=project_num).order_by('order_Number_Unique_ID')
    lastcount = purchase_order.count() + 1

    context = {
        "project_info": project_info,
        "proj_task": proj_task,
        "bom_info": BOM_info,
        "bom_type_list": BOM_type,
        "purchase_order": purchase_order,
        "stage": stage,
        "lastcount": lastcount,
    }

    return render(request, "project/dashboard_view.html", context)


def project_task_view(request, project_num, *args, **kwargs):
    project_info = Project.objects.filter(project_Number=project_num)

    stage = Stage.objects.filter(projecttasks__project_Number=project_num).distinct().order_by('stage_Order')
    proj_task = ProjectTasks.objects.filter(project_Number=project_num)

    context = {
        "project_info": project_info,
        "proj_task": proj_task,
        "stage": stage,
    }

    return render(request, "project_tasks/project_task_view.html", context)

def project_create_view(request):

    if request.method == 'POST':
        form = ProjectCreateForm(request.POST or None)
        if form.is_valid():
            obj = form.save()
            return redirect('/project/')

    form = ProjectCreateForm()
    context = {"form": form}
    return render(request, "project/project_create_view.html", context)

def project_update_view(request, project_num):
    obj = Project.objects.get(project_Number=project_num)
    form = ProjectUpdateForm(instance=obj)
    if request.method == 'POST':
        form = ProjectUpdateForm(request.POST or None, instance=obj)
        if form.is_valid():
            obj = form.save()
            return redirect('/project/dashboard/' + project_num)
        else:
            print(form.errors)

    context = {"form": form, "project": project_num}
    return render(request, "project/project_update_view.html", context)


def project_tasks_create_view(request, project_num):
    initialarr = {'project_Number': project_num}
    if request.method == 'POST':
        form = ProjectTasksCreateForm(request.POST or None)
        if form.is_valid():
            obj = form.save()
            return redirect('/project/dashboard/project_task/' + project_num + '/')

    form = ProjectTasksCreateForm(request.POST or None, initial=initialarr)
    context = {
        "form": form,
        "project": project_num
        }

    return render(request, "project_tasks/project_tasks_create_view.html", context)

def project_tasks_update_view(request, project_num, id):
    obj = ProjectTasks.objects.get(id=id)
    if request.method == 'POST':
        form = ProjectTasksCreateForm(request.POST or None, instance=obj)
        if form.is_valid():
            obj = form.save()
            return redirect('/project/dashboard/project_task/' + project_num + '/')

    form = ProjectTasksCreateForm(request.POST or None, instance=obj)
    context = {
        "form": form,
        "project": project_num,
        }

    return render(request, "project_tasks/project_tasks_update_view.html", context)

def project_tasks_delete_view(request, project_num, id):
    project_task = ProjectTasks.objects.get(id=id)
    if request.method == "POST":
        project_task.delete()
        return redirect('/project/dashboard/project_task/' + project_num + '/')
    context = {
        "project_task" : project_task,
        "project": project_num,
        "id": id,
        }

    return render(request, "project_tasks/project_tasks_delete_view.html", context)

def project_tasks_type_create_view(request, project_num):
    
    if request.method == 'POST':
        form = TasksTypeCreateForm(request.POST or None)
        if form.is_valid():
            obj = form.save()
            return redirect('/project/dashboard/project_task/' + project_num + '/')

    form = TasksTypeCreateForm()
    context = {
        "form": form,
        "project": project_num
        }
    return render(request, "project_tasks/project_tasks_type_create_view.html", context)

def project_resource_create_view(request, project_num):
    
    if request.method == 'POST':
        form = ResourceCreateForm(request.POST or None)
        if form.is_valid():
            obj = form.save()
            return redirect('/project/dashboard/project_task/' + project_num + '/')

    form = ResourceCreateForm()
    context = {
        "form": form,
        "project": project_num
        }
    return render(request, "project_tasks/project_resource_name_create_view.html", context)

def project_task_pdf_view(request, project_num, *args, **kwargs):
    project_info = Project.objects.filter(project_Number=project_num)

    stage = Stage.objects.filter(projecttasks__project_Number=project_num).distinct().order_by('stage_Order')
    proj_task = ProjectTasks.objects.filter(project_Number=project_num)

    context = {
        "test": "test",
        "project_info": project_info,
        "proj_task": proj_task,
        "stage": stage,
    }

    pdf = render_to_pdf('project_tasks/project_tasks_pdf_view.html', context)
    return HttpResponse(pdf, content_type='application/pdf')