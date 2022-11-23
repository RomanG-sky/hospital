from django.contrib import admin
from new_hospital.models import Doctor
from new_hospital.models import Medical_speciality
from new_hospital.models import Hospital

class DoctorModelAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'sex', 'rang', 'photo', 'email', 'date_of_birth', 'experience',)
    list_filter = ('last_name', 'experience', 'date_of_birth')
    filter_horizontal = ('education',)
    list_per_page = 10
    prepopulated_fields = {'slug': ('rang', 'last_name', 'first_name')}
    ordering = ('last_name','experience',)


class Medical_specialityModelAdmin(admin.ModelAdmin):
    list_display = ('speciality',)
    list_filter = ('speciality',)
    list_per_page = 20
    prepopulated_fields = {'slug': ('speciality',)}
    ordering = ('speciality',)


class HospitalModelAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'cabinet', 'description',)
    filter_horizontal = ('hospital_department',)
    list_filter = ('doctor', 'hospital_department')
    list_per_page = 20
    ordering = ('hospital_department',)


admin.site.register(Medical_speciality, Medical_specialityModelAdmin)
admin.site.register(Doctor, DoctorModelAdmin)
admin.site.register(Hospital, HospitalModelAdmin)
