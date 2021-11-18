from django.db import models
from customer.models import Customer
from employee.models import Employee


# Create your models here.

class Project(models.Model):
    project_Number              = models.CharField(max_length=20, primary_key=True)
    project_description         = models.TextField(null=True, blank=True)
    customer_Project            = models.ForeignKey(Customer, on_delete=models.PROTECT)
    order_Number                = models.CharField(max_length=20)
    project_Lead                = models.ForeignKey(Employee, on_delete=models.PROTECT)
    order_Date                  = models.DateField(blank=True, null=True)
    delivery_Date               = models.DateField(blank=True, null=True)
    completion_Date             = models.DateField(blank=True, null=True)
    started_Project             = models.BooleanField(default=False, blank=True, null=True)
    installed_Delivered         = models.BooleanField(default=False, blank=True, null=True)
    completed                   = models.BooleanField(default=False, blank=True, null=True)
    requires_Control_Panel      = models.BooleanField(default=False, blank=True, null=True)
    reason_For_Hold             = models.TextField(blank=True)
    no_Description              = models.TextField(blank=True)
    payment_Stage_Added         = models.BooleanField(default=False, blank=True, null=True)
    site_address_delivery       = models.TextField(blank=True)
    order_count                 = models.IntegerField(blank=True, null=True)
    project_Type                = models.CharField(max_length=20, choices=[('project', 'Project'), ('time and materials', 'Time and Materials')], blank=True, null=True)
    initial_Value               = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True, default=0)
    install_Start               = models.DateField(blank=True, null=True)
    install_Finish              = models.DateField(blank=True, null=True)
    launch                      = models.DateField(blank=True, null=True)
    completion_percentage       = models.DecimalField(max_digits=5, decimal_places=2, default=0, blank=True, null=True)
    days_To_Install             = models.IntegerField(blank=True, null=True)
    additional_Notes            = models.TextField(blank=True, null=True)
    file                        = models.FileField(upload_to='Project_Uploads/', blank=True, null=True)

    def __str__(self):
        return self.project_Number

    class Meta:
        verbose_name_plural = 'Projects'


class Project_Milestones(models.Model):
    milestone                   = models.CharField(max_length=50)
    project_number              = models.ForeignKey(Project, on_delete=models.CASCADE)
    milestone_Date              = models.DateField()
    label                       = models.CharField(max_length=120, null=True, blank=True)

    def __str__(self):
        return str(self.project_number) + ' ' + str(self.milestone)

    class Meta:
        verbose_name_plural = 'Project_Milestones'

class Stage_Payment_Description(models.Model):
    stage_Payment_Description   = models.CharField(max_length=120, primary_key=True)

    def __str__(self):
        return self.stage_Payment_Description

    class Meta:
        verbose_name_plural = 'Stage_Payments_Descriptions'

class Stage_Payment(models.Model):
    stage_Percentage            = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    project_number              = models.ForeignKey(Project, on_delete=models.PROTECT)
    can_Be_Invoiced             = models.BooleanField()
    stage_Payment_Description   = models.ForeignKey(Stage_Payment_Description, on_delete=models.CASCADE)
    stage_Authorised_By         = models.ForeignKey(Employee, on_delete=models.PROTECT)
    extra_Add_To_Order          = models.BooleanField(blank=True, null=True)
    extra_Value                 = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    extra_Description           = models.TextField(blank=True, null=True)
    new_Order_No                = models.CharField(max_length=50, blank=True, null=True)
    stage_Invoiced_And_Done     = models.BooleanField()
    customer_Order              = models.FileField(upload_to='Customer_Uploads/', blank=True, null=True)
    notes                       = models.TextField(null=True, blank=True)
    date_Of_Invoice             = models.DateField()

    def __str__(self):
        return str(self.project_number) + ' ' + str(self.date_Of_Invoice)

    class Meta:
        verbose_name_plural = 'Stage_Payments'

class Stage(models.Model):
    stage_Name                  = models.CharField(max_length=120, primary_key=True)
    stage_Order                 = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.stage_Name

    class Meta:
        verbose_name_plural = 'Stage_Project_Tasks'


class TaskType(models.Model):
    task_Type_Name                  = models.CharField(max_length=120, primary_key=True)

    def __str__(self):
        return self.task_Type_Name

    class Meta:
        verbose_name_plural = 'Tasks_Project_Tasks'

class ResourceNames(models.Model):
    resource_Names                  = models.CharField(max_length=120, primary_key=True)

    def __str__(self):
        return self.resource_Names

    class Meta:
        verbose_name_plural = 'Resource_Names_Project_Tasks'

class ProjectTasks(models.Model):
    project_Number                  = models.ForeignKey(Project, on_delete=models.PROTECT, null=True)
    stage                           = models.ForeignKey(Stage, on_delete=models.PROTECT, null=True)
    task_Type                       = models.ForeignKey(TaskType, on_delete=models.PROTECT, null=True)
    duration                        = models.IntegerField(null=True, blank=True)
    start_Date                      = models.DateField(blank=True, null=True)
    finish_Date                     = models.DateField(blank=True, null=True)
    percent_Complete                = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True, default=0)
    resource_Name                   = models.ForeignKey(ResourceNames, on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return str(self.project_Number) + ' ' + str(self.task_Type) + ' ' + str(self.percent_Complete) + '%'

    class Meta:
        verbose_name_plural = 'Project_Tasks'


class Tasks(models.Model):
    project_Number                  = models.ForeignKey(Project, on_delete=models.PROTECT, null=True)
    project_Description             = models.CharField(max_length=120, blank=True, null=True)
    task_Name                       = models.TextField(primary_key=True)
    task_Owner                      = models.ForeignKey(Employee, on_delete=models.PROTECT, null=True, related_name='task_Owner')
    task_Added_On                   = models.DateField(null=True)
    task_Added_By                   = models.ForeignKey(Employee, on_delete=models.PROTECT, null=True, related_name='task_Added_By')
    urgent_Task                     = models.BooleanField(default=False, null=True)
    task_Completion_Target_Date     = models.DateField(blank=True, null=True)
    task_Done                       = models.BooleanField(default=False, null=True)
    task_Completed_Date             = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.project_Number) + ' ' + str(self.project_Description) + '  Urgent: ' + str(self.urgent_Task)

    class Meta:
        verbose_name_plural = 'Tasks'


class SiteReports(models.Model):
    project_Number                  = models.ForeignKey(Project, on_delete=models.PROTECT, null=True)
    report_Date                     = models.DateField(null=True)
    site                            = models.CharField(max_length=120, null=True, blank=True)
    machine_equipment               = models.CharField(max_length=120, null=True)
    customer                        = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True)
    actions_Observations            = models.TextField(blank=True, null=True)
    advisory                        = models.TextField(blank=True, null=True)
    attach_Data_File                = models.FileField(upload_to='Site_Reports_Uploads/', blank=True, null=True)
    time_Of_Arrival                 = models.TimeField(blank=True, null=True)
    time_Of_Departure               = models.TimeField(blank=True, null=True)
    travel_To_From_Site_Hours       = models.DecimalField(max_digits=6, decimal_places=2)
    mileage_Total                   = models.DecimalField(max_digits=7, decimal_places=2)
    hcs_Engineer                    = models.ForeignKey(Employee, on_delete=models.PROTECT, null=True)
    hcs_Engineer_Sign               = models.TextField(blank=True, null=True)
    client_Representative_Full_Name = models.CharField(max_length=120, blank=True, null=True)
    client_Representative_Phone     = models.IntegerField(blank=True, null=True)
    client_Representative_Sign      = models.TextField(blank=True, null=True)
    invoice_Possible                = models.BooleanField(null=True)
    processed_By_Office             = models.BooleanField(null=True)
    processed_By_Office_Date        = models.DateField(blank=True, null=True)

    def __str__(self):
        return str(self.project_Number) + ' ' + str(self.site) + ' ' + str(self.customer)

    class Meta:
        verbose_name_plural = 'Site_Reports'

class WorkInstruction(models.Model):
    designation                     = models.CharField(max_length=50, blank=True, null=True)
    auto_Increment                  = models.AutoField(primary_key=True)
    project_Number                  = models.ForeignKey(Project, on_delete=models.PROTECT, null=True)
    customer                        = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True)
    start_Date_Time                 = models.CharField(max_length=120, blank=True, null=True)
    technical_Staff                 = models.ForeignKey(Employee, on_delete=models.PROTECT, null=True)
    file                            = models.FileField(upload_to='Work_Instruction_File_Upload/', blank=True, null=True)
    site_Contact                    = models.CharField(max_length=120, null=True, blank=True)
    site_Contact_Number             = models.IntegerField(blank=True, null=True)
    site_Address                    = models.TextField(blank=True, null=True)
    site_Name                       = models.CharField(max_length=120, blank=True, null=True)
    work_Description                = models.TextField(null=True)
    materials_Requirement           = models.TextField(blank=True, null=True)
    additional_Information          = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.project_Number) + '-' + str(self.auto_Increment)

    class Meta:
        verbose_name_plural = 'Work_Instructions'