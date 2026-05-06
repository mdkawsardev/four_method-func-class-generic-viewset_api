from django.contrib import admin
from classView.models import Citizen

@admin.register(Citizen)
class CitizenAdmin(admin.ModelAdmin):
    list_display = ["National_Id"]
