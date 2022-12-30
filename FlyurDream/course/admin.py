from django.contrib import admin
from .models import Course, Intake_Month, Course_Status, Course_Level, Intake_Year, Document, Course_Requirement
from import_export.admin import ImportExportMixin
# Register your models here.

# class CourseAdmin(ImportExportMixin, admin.ModelAdmin):
#     fieldsets = [
#         (None, {
#
#             'fields': ['country', 'course_level', 'course_name', 'course_image', 'course_intake_month', 'course_intake_year', 'documents_required', 'course_requirements', 'course_status'],
#         }),
#         # ('More Details', {
#         #     'fields': ['course_intake_month', 'course_intake_year', 'documents_required', 'course_requirements',
#         #                'course_status'],
#         # }),
#
#     ]
# admin.site.register(Course,CourseAdmin)

class CourseAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ('country', 'course_level', 'course_name',
                    )
    fieldsets = [
        ('Course', {
            'fields': ['country', 'course_level', 'course_name', 'course_image', 'course_intake_month', 'course_intake_year', 'documents_required', 'course_requirements', 'course_status'],
        }),
    ]
admin.site.register(Course, CourseAdmin),

class Intake_MonthAdmin(ImportExportMixin,admin.ModelAdmin):
    list_display = ['name']
    fieldsets = [
        ('Course', {
            'fields': ['name'],
        }),
    ]
admin.site.register(Intake_Month, Intake_MonthAdmin),


class Course_StatusAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name']
    fieldsets = [
        ('Course', {
            'fields': ['name'],
        }),
    ]
admin.site.register(Course_Status, Course_StatusAdmin),

class Course_LevelAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name']
    fieldsets = [
        ('Course', {
            'fields': ['name'],
        }),
    ]
admin.site.register(Course_Level, Course_LevelAdmin),

class Intake_YearAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name']
    fieldsets = [
        ('Course', {
            'fields': ['name'],
        }),
    ]
admin.site.register(Intake_Year, Intake_YearAdmin),

class DocumentAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name']
    fieldsets = [
        ('Course', {
            'fields': ['name'],
        }),
    ]
admin.site.register(Document, DocumentAdmin),

class Course_RequirementAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['name']
    fieldsets = [
        ('Course', {
            'fields': ['name'],
        }),
    ]
admin.site.register(Course_Requirement, Course_RequirementAdmin),
