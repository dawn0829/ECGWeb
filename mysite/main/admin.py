from django.contrib import admin
from .models import ECGdata,ECGList
# Register your models here.
admin.site.register(ECGList)
admin.site.register(ECGdata)
