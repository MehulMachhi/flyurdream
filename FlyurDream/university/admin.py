from django.contrib import admin
from .models import University
from import_export.admin import ImportExportMixin

# Register your models here.

class UniversityAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ['univ_name', 'country', 'univ_desc']
    fieldsets = [
        ('Course', {
            'fields': ['univ_name', 'country', 'univ_desc', 'univ_logo', 'select_default_assign_employee', 'univ_address', 'univ_phone', 'univ_email', 'univ_web', 'course'],
        }),
    ]
admin.site.register(University, UniversityAdmin),


# admin.site.register(University)

