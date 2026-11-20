"""booking/admin.py"""

from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'tdate', 'month_name', 'booked_at')
    list_filter = ('month_name',)
    search_fields = ('user__email', 'month_name')
    ordering = ('-booked_at',)
    date_hierarchy = 'booked_at'
