from django.contrib import admin
from django.contrib.admin.decorators import register

# Register your models here.
from .models import LACSalesTeam, LACQuotePortal

admin.site.register(LACQuotePortal)
admin.site.register(LACSalesTeam)