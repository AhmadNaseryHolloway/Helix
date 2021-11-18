from django.contrib import admin

# Register your models here.

from .models import po_WithoutProjects, NominalCode, POLineItems, PurchaseOrder, Suppliers

admin.site.register(po_WithoutProjects)
admin.site.register(NominalCode)
admin.site.register(POLineItems)
admin.site.register(PurchaseOrder)
admin.site.register(Suppliers)