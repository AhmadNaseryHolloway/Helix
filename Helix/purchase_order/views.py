from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import PurchaseOrderCreate, POLineItemCreate
from .models import PurchaseOrder, POLineItems
from Helix.utlis import render_to_pdf
from decimal import Decimal
from stock.models import StockItems

# Create your views here.

def purchase_order_dashboard_view(request, project_num, order_number, *args, **kwargs):

    purchase_order = PurchaseOrder.objects.filter(project_Number=project_num).order_by('order_Number_Unique_ID')
    lastcount = purchase_order.count() + 1
    po_line_items = POLineItems.objects.filter(purchase_Order=order_number)
    current = purchase_order.get(order_Number=order_number)
    context = {
        "project_info": project_num,
        "order_number": order_number,
        "purchase_order": purchase_order,
        "po_line_items": po_line_items,
        "current": current,
        "lastcount": lastcount,
    }
    return render(request, "purchaseOrder/purchase_order_dashboard.html", context)


def purchase_order_create(request, project_num, counter, *args, **kwargs):
    initialarr = {'project_Number': project_num, 'order_Number_Unique_ID': counter, 'order_Number': project_num + '-' + counter}


    if request.method == 'POST':
        form = PurchaseOrderCreate(request.POST or None, initial=initialarr)
        if form.is_valid():
            obj = form.save()
            return redirect('/purchaseorder/dashboard/' + project_num + '/' + obj.order_Number)
        else:
            print(form.errors)

    form = PurchaseOrderCreate(request.POST or None, initial=initialarr)
    context = {
        "form": form,
        "project_info": project_num,
        "order_Num": project_num + '-1',
    }
    return render(request, "purchaseOrder/purchase_order_create.html", context)

def purchase_order_po_line_create(request, project_num, order_number, *args, **kwargs):
    initialarr = {'purchase_Order': order_number}


    if request.method == 'POST':
        form = POLineItemCreate(request.POST or None, initial=initialarr)
        if form.is_valid():
            partnum = form.cleaned_data['stock_Item']            
            stock = StockItems.objects.get(part_Number=partnum)
            obj = form.save(commit=False)
            obj.line_Total = stock.net_Cost_Each * Decimal.from_float(obj.quantity)
            obj.save()
            return redirect('/purchaseorder/dashboard/' + project_num + '/' + order_number)
        else:
            print(form.errors)

    form = POLineItemCreate(request.POST or None, initial=initialarr)
    context = {
        'form': form,
        'order_Number': order_number,
        'project_num': project_num,
    }
    return render(request, "purchaseOrder/purchase_order_po_line_create.html", context)

def purchase_order_view_PDF_view(request, order):

    purchase_order = PurchaseOrder.objects.get(order_Number=order)
    po_line = POLineItems.objects.filter(purchase_Order=order)

    context = {
        "order": order,
        "purchase": purchase_order,
        "po_line": po_line,
    }
    pdf = render_to_pdf('purchaseOrder/purchase_order_pdf_view.html', context)
    return HttpResponse(pdf, content_type='application/pdf')