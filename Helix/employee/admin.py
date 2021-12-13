from django.contrib import admin

# Register your models here.
from .models import Accounts, AssetRegister, Branch, Employee, Contractors, Schedule, TimeType

admin.site.register(Accounts)
admin.site.register(Branch)
admin.site.register(Employee)
admin.site.register(AssetRegister)
admin.site.register(Contractors)
admin.site.register(TimeType)
admin.site.register(Schedule)