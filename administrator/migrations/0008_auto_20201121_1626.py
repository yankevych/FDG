# Generated by Django 3.1.3 on 2020-11-21 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0007_auto_20201121_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schema',
            name='string_character',
            field=models.CharField(blank=True, choices=[('"', '"'), ("'", "'")], max_length=10, null=True),
        ),
    ]
