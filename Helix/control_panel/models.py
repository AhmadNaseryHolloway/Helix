from django.db import models
from employee.models import Employee, Branch
from project.models import Project
# Create your models here.

class ControlsPanels(models.Model):
    control_Panel_Designation                   = models.CharField(max_length=120, null=True)
    project_Number                              = models.ForeignKey(Project, on_delete=models.PROTECT)
    project_Description                         = models.CharField(max_length=120, null=True)
    build_Technician                            = models.ForeignKey(Employee, on_delete=models.PROTECT)
    required_By_Date                            = models.DateField(blank=True, null=True)
    drawings                                    = models.FileField(upload_to='Control_Panel_Drawings_Upload/')
    started                                     = models.BooleanField(default=False, null=True)
    completed                                   = models.BooleanField(default=False, null=True)
    control_Panel_Calender_Label                = models.TextField(blank=True, null=True)
    late                                        = models.BooleanField(default=False, null=True)
    branch                                      = models.ForeignKey(Branch, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.project_Number) + ' ' + str(self.control_Panel_Designation) + ' ' + str(self.branch)

    class Meta:
        verbose_name_plural = 'Control_Panels'

class TestCertificate(models.Model):
    project_Number                              = models.ForeignKey(Project, on_delete=models.PROTECT, null=True)
    control_Panel                               = models.ForeignKey(ControlsPanels, on_delete=models.PROTECT)
    test_Engineer                               = models.ForeignKey(Employee, on_delete=models.PROTECT, null=True, related_name='test_Engineer')
    checked_By                                  = models.ForeignKey(Employee, on_delete=models.PROTECT, null=True, related_name='checked_By')
    test_Date                                   = models.DateField(blank=True, null=True)
    push_Buttons_Legends_Fitted                 = models.BooleanField(default=False, null=True)
    voltage_Warning_Lables_Fitted               = models.BooleanField(default=False, null=True)
    earth_Bonding_To_Door_And_Enclosure         = models.BooleanField(default=False, null=True)
    earth_Bonding_Stickers_Fitted               = models.BooleanField(default=False, null=True)
    fuses_Fitted                                = models.BooleanField(default=False, null=True)
    isolated_Shrouds_Fitted                     = models.BooleanField(default=False, null=True)
    isolator_Handle_Operation_Tested            = models.BooleanField(default=False, null=True)
    rj45_Patch_Leads_Fitted                     = models.BooleanField(default=False, null=True)
    earth_Continuity_1_or_Less                  = models.DecimalField(max_digits=3, decimal_places=3, null=True)
    continuity_Of_Main_Conductors_L1_1_Or_Less  = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    continuity_Of_Main_Conductors_L2_1_Or_Less  = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    continuity_Of_Main_Conductors_L3_1_Or_Less  = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    continuity_Of_Main_Conductors_N_1_Or_Less   = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    Control_Panel_Voltage_Supply_Max_Rating_V   = models.IntegerField(null=True)
    Control_Voltage_Actual_Reading_V            = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    supply_To_All_Devices_Checked               = models.BooleanField(default=False,null=True)
    safety_Relay_Functional_Test_Done           = models.BooleanField(default=False,null=True)
    indication_LEDs_Tested                      = models.BooleanField(default=False,null=True)
    push_Buttons_Tested                         = models.BooleanField(default=False,null=True)
    point_To_Point_Test_Completed               = models.BooleanField(default=False,null=True)
    termination_tug_Test_Completed              = models.BooleanField(default=False,null=True)
    inverters_Programmed                        = models.BooleanField(default=False,null=True)
    plc_Program_Loaded                          = models.BooleanField(default=False,null=True)
    tested_Stickers_Fitted                      = models.BooleanField(default=False,null=True)
    notes                                       = models.TextField(blank=True, null=True)
    signature                                   = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.project_Number) + ' ' + str(self.control_Panel)