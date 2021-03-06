from django.conf import settings
from django.db import models


class Schema(models.Model):
    """schema model"""
    SEPARATORS = [
        ('Comma (,)', 'Comma (,)'),
        ('Dot (.)', 'Dot (.)'),
    ]

    STRINGS = [
        ('Double-quote (")', 'Double-quote (")'),
        ("Single-quote (')", "Single-quote (')")
    ]

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    column_separator = models.CharField(max_length=50, null=True, blank=True, choices=SEPARATORS)
    string_character = models.CharField(max_length=50, null=True, blank=True, choices=STRINGS)
    name = models.CharField(max_length=50, null=True, blank=True)
    modified = models.DateField(auto_now=True)


class ColumnItem(models.Model):
    """model that add another column to schema"""
    TYPES = [
        ('Full name', 'Full name'),
        ('Integer', 'Integer'),
        ('Job', 'Job'),
        ('Company name', 'Company name'),
        ('Date', 'Date'),
    ]

    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, verbose_name="Schema")
    column_type = models.CharField(max_length=20, null=True, blank=True, choices=TYPES)
    column_name = models.CharField(max_length=50, null=True, blank=True)
    order = models.PositiveSmallIntegerField(null=True, blank=True)
    range_from = models.PositiveIntegerField(null=True, blank=True, default=0)
    range_to = models.PositiveIntegerField(null=True, blank=True, default=2147483647)

    class Meta:
        ordering = ['order']


class DataSet(models.Model):
    """model that contain data-sets"""
    STATUS = [
        ('Ready', 'Ready'),
        ('Processing', 'Processing'),
        ('Create', 'Create')
    ]
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, verbose_name="Schema")
    created = models.DateField(auto_now=True)
    rows = models.PositiveSmallIntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, default='Create', choices=STATUS)
    file_name = models.CharField(max_length=100, null=True, blank=True)


