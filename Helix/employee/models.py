from django.conf import settings
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.expressions import F

# Create your models here.

class Branch(models.Model):
    branch_Name                 = models.CharField(max_length=30, primary_key=True)
    address                     = models.TextField(blank=True, null=True)
    phone                       = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.branch_Name

    class Meta:
        verbose_name_plural = 'Branchs'

class Accounts(models.Model):
    account                     = models.CharField(max_length=30)

    def __str__(self):
        return self.account

    class Meta:
        verbose_name_plural = 'Accounts'


class Employee(models.Model):
    employeeName                = models.CharField(max_length=120)
    username                    = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    email                       = models.EmailField(unique=True)
    gender                      = models.CharField(max_length=6, choices=[('male', 'Male'), ('female', 'Female')])
    position                    = models.CharField(max_length=120)
    phone                       = models.CharField(max_length=20)
    address                     = models.TextField()
    notes                       = models.TextField(blank=True, null=True)
    contracted_start_time       = models.TimeField(auto_now=False, auto_now_add=False)
    contracted_finish_time      = models.TimeField(auto_now=False, auto_now_add=False)
    branch_location             = models.CharField(max_length=120)
    account                     = models.CharField(max_length=120)
    standard_hours              = models.IntegerField(blank=True, null=True)
    annual_Allowance            = models.IntegerField(blank=True, null=True)
    annual_Allowance_remaining  = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.employeeName

    class Meta:
        verbose_name_plural = 'Employees'


class AssetRegister(models.Model):
    tool_Description            = models.CharField(max_length=120, blank=True, null=True)
    serial_Number               = models.CharField(max_length=120, blank=True, null=True)
    date_Of_Issue               = models.DateField(blank=True, null=True)
    tool_Owner                  = models.ForeignKey(Employee, on_delete=models.PROTECT)
    text_formula                = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return str(self.tool_Description) + ' ' + str(self.tool_Owner)

    class Meta:
        verbose_name_plural = 'AssetRegister'


class Contractors(models.Model):
    auto_increment              = models.AutoField(primary_key=True)
    name                        = models.CharField(max_length=120, blank=True, null=True)
    email                       = models.EmailField(blank=True, null=True)
    phone_1                     = models.IntegerField(blank=True, null=True)
    phone_2                     = models.IntegerField(blank=True, null=True)
    skill_Set                   = models.TextField(blank=True, null=True)
    detailed_information        = models.TextField(blank=True, null=True)
    data_File                   = models.FileField(upload_to='Contractors_File_Uploads/', blank=True, null=True)
    approve                     = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contractors'

class TimeType(models.Model):
    name                        = models.CharField(max_length=120, primary_key=True)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    id                          = models.AutoField(primary_key=True)
    employee                    = models.ForeignKey(Employee, on_delete=CASCADE, null=True)
    time_Type                   = models.ForeignKey(TimeType, on_delete=PROTECT, null=True)
    holiday                     = models.BooleanField(default=False, null=True)
    start_Date                  = models.DateField(null=True)
    end_Date                    = models.DateField(null=True)
    start_Time                  = models.TimeField(blank=True, null=True)
    end_Time                    = models.TimeField(blank=True, null=True)
    weekend                     = models.BooleanField(default=False, null=True)
    reason                      = models.CharField(max_length=120, blank=True, null=True)
