from django.db import models
from stock.models import StockItems
from purchase_order.models import Suppliers
from project.models import Project
# Create your models here.

class BOMType(models.Model):
    bom_Type                    = models.CharField(max_length=120, primary_key=True)
    project_Number              = models.ForeignKey(Project, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.bom_Type
    
    class Meta:
        verbose_name_plural = 'BOM_Type_List'



class SubSection(models.Model):
    sub_Section_Name            = models.CharField(max_length=120, primary_key=True)

    def __str__(self):
        return self.sub_Section_Name
    
    class Meta:
        verbose_name_plural = 'BOM_Sub_Sections'


class BOM(models.Model):
    id                          = models.AutoField(primary_key=True)
    bom_type                    = models.ForeignKey(BOMType, on_delete=models.PROTECT, null=True, blank=True)
    project_Number              = models.ForeignKey(Project, on_delete=models.PROTECT)
    sub_Section                 = models.ForeignKey(SubSection, on_delete=models.PROTECT, blank=True, null=True)
    item_Number                 = models.ForeignKey(StockItems, on_delete=models.PROTECT, blank=True, null=True)
    quantity                    = models.FloatField(default=0, null=True)
    total_Price                 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    order_Number_Unique_ID      = models.CharField(max_length=120, blank=True, null=True)
    delivery_Date               = models.DateField(blank=True, null=True)
    supplier                    = models.ForeignKey(Suppliers, on_delete=models.PROTECT, blank=True, null=True)


    def __str__(self):
        return str(self.item_Number) + str(self.project_Number)
    
    class Meta:
        verbose_name_plural = 'BOMs'