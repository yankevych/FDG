# Generated by Django 3.1.3 on 2020-11-21 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0008_auto_20201121_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schema',
            name='column_separator',
            field=models.CharField(blank=True, choices=[(',', 'Comma (,)'), ('.', 'Dot (.)')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='schema',
            name='rows',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='schema',
            name='string_character',
            field=models.CharField(blank=True, choices=[('"', 'Double-quote (")'), ("'", "Single-quote (')")], max_length=10, null=True),
        ),
    ]
