from django.db import models
from employee.models import Employee
from customer.models import Customer

# Create your models here.

class LACSalesTeam(models.Model):
    name                = models.CharField(max_length=50)
    email               = models.EmailField()
    phone               = models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'LAC_Sales_Teams'

class LACQuotePortal(models.Model):
    header                          = models.CharField(max_length=120)
    lac_reference                   = models.CharField(max_length=120)
    lac_description                 = models.TextField()
    category_Of_Quote               = models.CharField(max_length=10,choices=[('Cat A', 'Cat A'), ('Cat B', 'Cat B'), ('Cat C', 'Cat C')])
    quote_Requested_By              = models.ForeignKey(LACSalesTeam, on_delete=models.PROTECT)
    holloway_Contact_connection     = models.ForeignKey(Employee, on_delete=models.PROTECT, blank=True)
    attachment_1                    = models.FileField(upload_to='LAC_Quote_Portal/', blank=True, null=True)
    attachment_2                    = models.FileField(upload_to='LAC_Quote_Portal/', blank=True, null=True)
    attachment_3                    = models.FileField(upload_to='LAC_Quote_Portal/', blank=True, null=True)
    status                          = models.CharField(max_length=120, choices=[('awaiting reply', 'Awaiting Reply'), ('in progress', 'In Progress'), ('quotation submitted', 'Quotation Submitted')])
    date_Of_Request                 = models.DateField(blank=True, null=True)
    quote_Required_By               = models.DateField()
    date_Of_Completion              = models.DateField(blank=True, null=True)
    general_Details                 = models.TextField(blank=True, null=True)
    motor_Control_details           = models.TextField(blank=True, null=True)
    pneumatics_Required             = models.BooleanField(null=True)
    wms_Interface_Required          = models.BooleanField()
    barcode_Reading_Required        = models.BooleanField()
    location_Within_Uk_Overseas     = models.CharField(max_length=120)
    installation_Required           = models.BooleanField()
    description_Header              = models.TextField()
    lac_Sales_Person                = models.CharField(max_length=120, blank=True, null=True)
    holloway_contact                = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.lac_reference + ' ' + self.lac_description + ' ' + self.quote_Requested_By
    
    class Meta:
        verbose_name_plural = 'LAC_Quote_Portal'

class QuoteNumbers(models.Model):
    QuoteNo                         = models.CharField(max_length=10)
    quote_No_Inc                    = models.AutoField(unique=True, primary_key=True)
    customer                        = models.ForeignKey(Customer, on_delete=models.PROTECT)
    employee                        = models.ForeignKey(Employee, on_delete=models.PROTECT)
    quote_Date                      = models.DateField()
    quote_Description               = models.TextField()
    recipient_Name                  = models.CharField(max_length=30)
    value                           = models.DecimalField(max_digits=15, decimal_places=2)
    lac_Quote_Portal                = models.ForeignKey(LACQuotePortal, on_delete=models.PROTECT)
    quote_Prepared_By               = models.CharField(max_length=30)