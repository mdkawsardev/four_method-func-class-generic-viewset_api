from django.contrib import admin
from funcView.models import Students
@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ["Name", "Age", "Department", "Created_At"]
