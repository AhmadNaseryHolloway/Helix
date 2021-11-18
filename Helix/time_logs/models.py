from django.db import models
from employee.models import Employee
from project.models import Project


# Create your models here.
class TimeLog(models.Model):
    auto_Increment              = models.AutoField(primary_key=True)
    project_Number              = models.ForeignKey(Project, on_delete=models.PROTECT, null=True)
    day                         = models.DateField(null=True)
    start_Time                  = models.TimeField(null=True)
    end_Time                    = models.TimeField(null=True)
    notes                       = models.TextField(null=True)
    weekend                     = models.IntegerField(choices=[(1, 1), (0, 0)], null=True)
    employee_Name               = models.ForeignKey(Employee, on_delete=models.PROTECT, null=True)
    flag                        = models.BooleanField(default=False, null=True)
    holiday                     = models.BooleanField(default=False, null=True)
    base_Time                   = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    result_Time                 = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    day_Of_Week                 = models.IntegerField(blank=True, null=True)
    overnight                   = models.BooleanField(default=False, null=True)
    aux_Name                    = models.CharField(max_length=120, default='temp', null=True)
    display                     = models.CharField(max_length=120, default='temp', null=True)
    overtime_Weekday            = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    employee                    = models.CharField(max_length=120, null=True, blank=True)


    def __str__(self):
        return str(self.employee_Name) + ' ' + str(self.result_Time)

    class Meta:
        verbose_name_plural = 'TimeLogs'