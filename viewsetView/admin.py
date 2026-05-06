from django.contrib import admin
from viewsetView.models import Fruits

@admin.register(Fruits)
class FruitsAdmin(admin.ModelAdmin):
    list_display = ["Name"]
