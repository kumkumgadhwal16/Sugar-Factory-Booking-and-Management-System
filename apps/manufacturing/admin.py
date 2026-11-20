"""manufacturing/admin.py"""

from django.contrib import admin
from .models import ManufacturingStage


@admin.register(ManufacturingStage)
class ManufacturingStageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'order')
    ordering = ('order',)
