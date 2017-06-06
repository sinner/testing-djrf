from django.db import models


class TimeStampable(models.Model):
    """TimeStampable"""
    STATUS_CHOICES = (
        ('A', 'Active'),
        ('I', 'Inactive')
    )

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        abstract = True
