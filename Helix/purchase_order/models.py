from django.db import models
from stock.models import StockItems
from employee.models import Branch, Employee
from project.models import Project
from stock.models import Products
from datetime import date

# Create your models here.

class Suppliers(models.Model):
    suppliers_Name              = models.CharField(max_length=50, primary_key=True)
    address                     = models.TextField(blank=True, null=True)
    phone                       = models.IntegerField(blank=True, null=True)
    email                       = models.EmailField(blank=True, null=True)
    primary_Contact_Sales       = models.CharField(max_length=50, blank=True, null=True)
    primary_Contact_Admin       = models.CharField(max_length=50, blank=True, null=True)
    primary_Contact_Technical   = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.suppliers_Name
    
    class Meta:
        verbose_name_plural = 'Suppliers'


class PurchaseOrder(models.Model):
    order_Number                = models.CharField(max_length=50, primary_key=True)
    project_Number              = models.ForeignKey(Project, on_delete=models.PROTECT)
    line_Item_Count             = models.IntegerField(blank=True, null=True)
    order_Number_Unique_ID      = models.CharField(max_length=15, blank=True, null=True)
    order_Date                  = models.DateField(null=True, default=date.today)
    delivery_Required_Date      = models.DateField(null=True)
    delivered_In_Full           = models.BooleanField(default=False)
    partial_Delivery            = models.BooleanField(default=False)
    instructions                = models.TextField(blank=True, null=True)
    order_Placed_By             = models.ForeignKey(Employee, on_delete=models.PROTECT, blank=True, null=True, related_name='order_placed_by')
    delivery_Address            = models.TextField(blank=True, null=True)
    order_Value_Total           = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    actual_Delivery_Date        = models.DateField(blank=True, null=True)
    terms                       = models.CharField(max_length=120, blank=True, null=True)
    sales_Tax                   = models.DecimalField(max_digits=4, decimal_places=3, default=0.20, blank=True, null=True)
    shipping_Handling           = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    requisitioner               = models.ForeignKey(Employee, on_delete=models.PROTECT, blank=True, null=True, related_name='requisitioner')
    receipt_PDF                 = models.FileField(upload_to='Purchase_Order_Receipt_PDF/', blank=True, null=True)
    completed_Date              = models.DateField(blank=True, null=True)
    checked_By                  = models.ForeignKey(Employee, on_delete=models.PROTECT, blank=True, null=True)
    delivered_To                = models.CharField(default='Telford', choices=[('Telford', 'Telford'), ('Nottingham', 'Nottingham'), ('other', 'other')], max_length=50)
    fao                         = models.CharField(max_length=120, null=True, blank=True, default="Holloway Controls")
    supplier                    = models.ForeignKey(Suppliers, on_delete=models.PROTECT, null=True)
    branch                      = models.ForeignKey(Branch, on_delete=models.PROTECT, blank=True, null=True)
    order_Notes                 = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.order_Number) + ' Delivered In Full: ' + str(self.delivered_In_Full)
    
    class Meta:
        verbose_name_plural = 'Purchase_Orders'

class NominalCode(models.Model):
    result                      = models.CharField(max_length=50, null=True)
    nominal_Code_No             = models.IntegerField(primary_key=True)
    description                 = models.CharField(max_length=50, default='Description')
    budget_Allowance            = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    budget_expenditure          = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    over_Budget                 = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    cost_Centre_Managers        = models.ForeignKey(Employee, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return str(self.nominal_Code_No) + ' ' + str(self.description)
    
    class Meta:
        verbose_name_plural = 'Nominal_Codes'

class po_WithoutProjects(models.Model):
    po_Number                   = models.CharField(max_length=120, default='HCS')
    inc_Number                  = models.AutoField(primary_key=True)
    date_Of_PO                  = models.DateField(blank=True, null=True)
    supplier                    = models.ForeignKey(Suppliers, on_delete=models.PROTECT, null=True)
    details                     = models.CharField(max_length=120, default='Details')
    nominal_Code                = models.ForeignKey(NominalCode, on_delete=models.PROTECT, null=True)
    order_Placed_By             = models.ForeignKey(Employee, on_delete=models.PROTECT, blank=True, null=True, related_name='order_Placed_By')
    authorised_By               = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='authorised_By')

    def __str__(self):
        return 'HCS' + str(self.inc_Number)
    
    class Meta:
        verbose_name_plural = 'PO_Without_Projects'

class POLineItems(models.Model):
    item_Number                 = models.IntegerField(blank=True, null=True)
    quantity                    = models.IntegerField(default=0, null=True)
    net_Cost_Each_ExVAT         = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    line_Total                  = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    purchase_Order              = models.ForeignKey(PurchaseOrder, on_delete=models.PROTECT, blank=True, null=True)
    product                     = models.ForeignKey(Products, on_delete=models.PROTECT, blank=True, null=True)
    part_Number                 = models.CharField(max_length=120, blank=True, null=True)
    description                 = models.TextField(default='Description', blank=True, null=True)
    stock_Item                  = models.ForeignKey(StockItems, on_delete=models.PROTECT, null=True)
    arrived                     = models.BooleanField(default=False, blank=True, null=True)
    qty_Arrived                 = models.IntegerField(blank=True, default=0, null=True)

    def __str__(self):
        return str(self.purchase_Order) + ' ' + str(self.stock_Item)
    
    class Meta:
        verbose_name_plural = 'PO_Line_Items'

