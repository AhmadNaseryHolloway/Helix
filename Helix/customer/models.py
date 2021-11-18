from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_Name               = models.CharField(max_length=120, primary_key=True)
    addresss                    = models.TextField()
    phone                       = models.CharField(max_length=30)

    def __str__(self):
        return self.customer_Name

    class Meta:
        verbose_name_plural = 'Customers'
