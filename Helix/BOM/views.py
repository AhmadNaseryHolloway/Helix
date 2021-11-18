from django.shortcuts import render, redirect
from decimal import Decimal
from stock.models import StockItems
from .forms import BOMCreateForm, BOMTypeCreateForm
from .models import BOMType, BOM

# Create your views here.
def bom_create_view(request, project_num, bom_type):
    if request.method == 'POST':
        form = BOMCreateForm(request.POST or None)
        if form.is_valid():
            partnum = form.cleaned_data['item_Number']            
            stock = StockItems.objects.get(part_Number=partnum)
            obj = form.save(commit=False)
            obj.total_Price = stock.net_Cost_Each * Decimal.from_float(obj.quantity)
            obj.save()
            return redirect('/project/bom/' + project_num + '/' + bom_type + '/')

    form = BOMCreateForm(initial={'project_Number': project_num, 'bom_type': bom_type})
    context = {
        "form": form,
        "project": project_num,
        "bom_type": bom_type
        }
    return render(request, "bom/bom_create_view.html", context)

def bom_type_create_view(request, project_num):
    if request.method == 'POST':
        form = BOMTypeCreateForm(request.POST or None)
        if form.is_valid():
            obj = form.save()
            return redirect('/project/bom/' + project_num + '/empty/')

    form = BOMTypeCreateForm(initial={'project_Number':project_num})
    context = {
        "form": form,
        "project": project_num
        }

    return render(request, "bom/bom_type_create_view.html", context)


def bom_type_update_view(request, project_num, bom_type):
    obj = BOMType.objects.get(project_Number=project_num, bom_Type=bom_type)
    form = BOMTypeCreateForm(instance=obj)
    if request.method == 'POST':
        form = BOMTypeCreateForm(request.POST or None, instance=obj)
        if form.is_valid():
            obj2 = form.save()
            return redirect('/project/bom/' + project_num + '/' + bom_type + '/')

    context = {
        "form": form,
        "project": project_num,
        "bom_type": bom_type
        }

    return render(request, "bom/bom_type_update_view.html", context)