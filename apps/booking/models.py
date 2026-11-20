"""
booking/models.py
id, user_id, tdate, month_name
"""

from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime


class Booking(models.Model):
    """
    A single cane delivery slot booking by a farmer/user.
    One user can book one slot per day; max 3 bookings per day total.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bookings',
        db_column='user_id'
    )
    tdate = models.IntegerField(verbose_name='Day of Month')           # e.g. 15
    month_name = models.CharField(max_length=50, verbose_name='Month') # e.g. "January 2024"
    booked_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'booking'
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
        # Prevent same user booking same day in same month
        unique_together = ('user', 'tdate', 'month_name')
        ordering = ['-booked_at']

    def __str__(self):
        return f"{self.user.email} — {self.tdate} {self.month_name}"

    @classmethod
    def is_slot_full(cls, tdate, month_name):
        """Returns True if the day already has MAX_SLOTS_PER_DAY bookings."""
        max_slots = getattr(settings, 'MAX_SLOTS_PER_DAY', 3)
        return cls.objects.filter(tdate=tdate, month_name=month_name).count() >= max_slots

    @classmethod
    def user_already_booked(cls, user, tdate, month_name):
        """Returns True if user has already booked that day in that month."""
        return cls.objects.filter(user=user, tdate=tdate, month_name=month_name).exists()

    def get_full_date_display(self):
        return f"{self.tdate} {self.month_name}"
