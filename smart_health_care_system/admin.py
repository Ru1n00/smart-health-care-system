from django.contrib import admin

from .models import Doctor, BloodDonor, Ambulance

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'speciality', 'degrees_earned', 'position', 'location', 'visiting_place', 'visiting_hours', 'contact_info', 'img')


class BloodDonorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'blood_group', 'location', 'contact_info')


class AmbulanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact_info', 'district')


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(BloodDonor, BloodDonorAdmin)
admin.site.register(Ambulance, AmbulanceAdmin)