from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Medicine)
admin.site.register(Doctor)
admin.site.register(Lab)
admin.site.register(Ambulance)
admin.site.register(Pharamacy)
admin.site.register(Family)
admin.site.register(Response)
# admin.site.register(Patient)
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','pin_code','ailment']

