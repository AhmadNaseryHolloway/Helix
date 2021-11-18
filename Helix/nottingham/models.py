from django.db import models
from employee.models import Employee
from project.models import Project
# Create your models here.

class NottinghamRatesLabour(models.Model):
    service_Type                    = models.CharField(max_length=120, primary_key=True)
    unit_Rate                       = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return str(self.service_Type) + ' ' + str(self.unit_Rate)

    class Meta:
        verbose_name_plural = 'Nottingham_Rates_Labour'

class NottinghamWorkRecord(models.Model):
    auto_Increment                  = models.AutoField(primary_key=True)
    project_Number                  = models.ForeignKey(Project, on_delete=models.PROTECT, null=True)
    day                             = models.DateField(null=True)
    start_Time                      = models.TimeField(null=True)
    end_Time                        = models.TimeField(null=True)
    notes                           = models.TextField(blank=True, null=True)
    employee                        = models.ForeignKey(Employee, on_delete=models.PROTECT, null=True)
    flag                            = models.BooleanField(default=False, null=True)
    base_Time                       = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    result_Time                     = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    calender_Label                  = models.CharField(max_length=120, blank=True, null=True)
    day_Of_Week                     = models.IntegerField(null=True, blank=True)
    overnight                       = models.BooleanField(default=False, null=True)
    weekend                         = models.IntegerField(null=True, choices=[(1,1), (0,0)])
    nottingham_Rate                 = models.ForeignKey(NottinghamRatesLabour, on_delete=models.PROTECT, null=True)
    labour_Total                    = models.DecimalField(max_digits=15, decimal_places=2, null=True, default=0)
    mileage                         = models.IntegerField(null=True, default=0)
    mileage_Total                   = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    accomodation_Total              = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    grand_Total                     = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    processed                       = models.BooleanField(default=False, null=True)
    authorised                      = models.BooleanField(default=False, null=True)

    def __str__(self):
        return str(self.project_Number) + ' ' + str(self.employee) + str(self.day)