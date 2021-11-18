from django.db import models
from employee.models import Employee, Branch
from project.models import Project


# Create your models here.

class StockManufacturer(models.Model):
    stock_Manufacturer_Name             = models.CharField(max_length=120, primary_key=True)

    def __str__(self):
        return self.stock_Manufacturer_Name

    class Meta:
        verbose_name_plural = 'Stock_Manufacturer'

class StockCategory(models.Model):
    stock_Category_Name                 = models.CharField(max_length=120, primary_key=True)

    def __str__(self):
        return self.stock_Category_Name

    class Meta:
        verbose_name_plural = 'Stock_Category'

class StockLocation(models.Model):
    stock_Location_Name                 = models.TextField(primary_key=True)
    notes                               = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.stock_Location_Name

    class Meta:
        verbose_name_plural = 'Stock_Location_Name'

class StockOwner(models.Model):
    stock_Owner_Name                    = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.stock_Owner_Name

    class Meta:
        verbose_name_plural = 'Stock_Owner'

class StockItems(models.Model):
    part_Number                         = models.CharField(max_length=120, primary_key=True)
    description                         = models.TextField()
    stock_Manufacturer                  = models.ForeignKey(StockManufacturer, on_delete=models.PROTECT)
    stock_Category                      = models.ForeignKey(StockCategory, on_delete=models.PROTECT)
    net_Cost_Each                       = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    line_Total_Sum                      = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    stock_Owner                         = models.ForeignKey(StockOwner, on_delete=models.PROTECT)
    long_Description                    = models.TextField(blank=True, null=True)
    stock_Balance_Telford               = models.IntegerField(blank=True, null=True)
    stock_Balance_Notts                 = models.IntegerField(blank=True, null=True)
    stock_Location                      = models.ForeignKey(StockLocation, on_delete=models.PROTECT, blank=True, null=True)
    stock_Level_Min                     = models.IntegerField(blank=True, null=True)
    stock_Level_Status                  = models.IntegerField(blank=True, null=True)
    branches                            = models.ForeignKey(Branch, on_delete=models.PROTECT, blank=True, null=True)
    stocked_At_Telford                  = models.BooleanField()
    stocked_At_Notts                    = models.BooleanField()

    def __str__(self):
        return self.part_Number

    class Meta:
        verbose_name_plural = 'Stock_Items'

class StockLog(models.Model):
    stock_Item                          = models.ForeignKey(StockItems, on_delete=models.PROTECT)
    project_Number                      = models.ForeignKey(Project, on_delete=models.PROTECT)
    removed_By                          = models.ForeignKey(Employee, on_delete=models.PROTECT)
    transaction_Date                    = models.DateField()
    qty_Removed                         = models.IntegerField(default=0, blank=True, null=True)
    qty_Added                           = models.IntegerField(default=0, blank=True, null=True)
    added_Total                         = models.IntegerField(default=0, blank=True, null=True)
    removed_Result                      = models.IntegerField(default=0, blank=True, null=True)
    value_Removed                       = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    description                         = models.TextField(blank=True, null=True)
    calender_Info                       = models.TextField(blank=True, null=True)
    branch                              = models.ForeignKey(Branch, on_delete=models.PROTECT, blank=True, null=True)
    bran                                = models.IntegerField(blank=True, null=True)
    branch_Location                     = models.CharField(max_length=120, choices=[('telford', 'Telford'), ('nottingham', 'Nottingham')], blank=True, null=True)

    def __str__(self):
        return str(self.project_Number) + ' ' + str(self.stock_Item) + ' ' + str(self.transaction_Date)

    class Meta:
        verbose_name_plural = 'Stock_Log'

class Products(models.Model):
    part_Number                         = models.CharField(max_length=120, primary_key=True)
    description                         = models.TextField(blank=True, null=True)
    stock_Manufacturer                  = models.ForeignKey(StockManufacturer, on_delete=models.PROTECT)
    stock_Category                      = models.ForeignKey(StockCategory, on_delete=models.PROTECT)
    description_Full                    = models.TextField(blank=True, null=True)
    discount_Percentage                 = models.DecimalField(default=0, max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return str(self.part_Number) + ' ' + str(self.description)