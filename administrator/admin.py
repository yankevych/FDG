from django.contrib import admin
from .models import Schema, ColumnItem, DataSet

admin.site.register(Schema)
admin.site.register(ColumnItem)
admin.site.register(DataSet)
