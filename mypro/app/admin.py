from django.contrib import admin
from .models import Department, Employee, EmployeeSalary

# Register your models here.

# admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(EmployeeSalary)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'floor')
    readonly_fields = ['display_reporting_hierarchy']

    def display_reporting_hierarchy(self, obj):
        return '<a href="/employees/department/{}/reporting/" target="_blank">View Hierarchy</a>'.format(obj.id)

    display_reporting_hierarchy.allow_tags = True


