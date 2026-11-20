"""
core/models.py
Static content models for editable About Us, Contact, Manager, Performance data.
"""

from django.db import models


class AboutUs(models.Model):
    """Editable About Us page content."""
    title = models.CharField(max_length=200, default='Navalsingh Sugar Factory')
    description = models.TextField(
        default='Navalsingh Sahakari Shakkar Karkhana Maryadit is a sugar '
                'manufacturing company established in 1981 by Thakur Shivkumar Singh.'
    )
    established_year = models.IntegerField(default=1981)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'about_us'
        verbose_name = 'About Us'

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    """Factory contact information."""
    address = models.CharField(max_length=300, default='Navalnagar(Jhiri), Burhanpur, MP')
    phone = models.CharField(max_length=20, default='+091000000087')
    email = models.EmailField(default='nssk.mp@gmail.com')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'contact_info'
        verbose_name = 'Contact Info'

    def __str__(self):
        return self.address


class Manager(models.Model):
    """Factory manager record."""
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    department = models.CharField(max_length=150, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    photo = models.ImageField(upload_to='managers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'manager'
        verbose_name = 'Manager'

    def __str__(self):
        return f"{self.name} — {self.designation}"


class PerformanceData(models.Model):
    """Annual performance metrics."""
    season_year = models.CharField(max_length=20)        # e.g. "2023-24"
    cane_crushed_mt = models.FloatField(default=0)       # metric tonnes
    sugar_produced_mt = models.FloatField(default=0)
    recovery_percent = models.FloatField(default=0)
    working_days = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'performance_data'
        verbose_name = 'Performance Data'
        ordering = ['-season_year']

    def __str__(self):
        return f"Season {self.season_year}"
