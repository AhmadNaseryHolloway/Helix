from django.contrib import admin

# Register your models here.
from .models import Accounts, AssetRegister, Branch, Employee, Contractors

admin.site.register(Accounts)
admin.site.register(Branch)
admin.site.register(Employee)
admin.site.register(AssetRegister)
admin.site.register(Contractors)