"""
manufacturing/models.py
Manufacturing process stage model.
"""

from django.db import models


class ManufacturingStage(models.Model):
    """Each stage of the sugar manufacturing process."""
    STAGES = [
        ('cane_yard', 'Cane Yard'),
        ('mill', 'Milling House'),
        ('boiler', 'Boiler House'),
        ('clarification', 'Clarification Section'),
        ('curing', 'Curing House'),
        ('crystalization', 'Crystallization'),
    ]
    slug = models.SlugField(unique=True, choices=STAGES)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='manufacturing/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'manufacturing_stage'
        ordering = ['order']
        verbose_name = 'Manufacturing Stage'

    def __str__(self):
        return self.title
