from django.contrib import admin
from genericView.models import Animals
@admin.register(Animals)
class AnimalsAdmin(admin.ModelAdmin):
    list_display = ["Name"]
