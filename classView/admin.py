from django.contrib import admin
from classView.models import Citizen, FileUpload

admin.site.register(FileUpload)
@admin.register(Citizen)
class CitizenAdmin(admin.ModelAdmin):
    list_display = ["National_Id"]
