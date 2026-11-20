"""core/admin.py"""

from django.contrib import admin
from .models import AboutUs, ContactInfo, Manager, PerformanceData


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'established_year', 'updated_at')


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone', 'email', 'updated_at')


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'department', 'phone')
    search_fields = ('name', 'designation')


@admin.register(PerformanceData)
class PerformanceDataAdmin(admin.ModelAdmin):
    list_display = ('season_year', 'cane_crushed_mt', 'sugar_produced_mt',
                    'recovery_percent', 'working_days')
    ordering = ('-season_year',)
