from django.contrib import admin

from .models import BOMType, BOM, SubSection

admin.site.register(BOM)
admin.site.register(BOMType)
admin.site.register(SubSection)
# Register your models here.
