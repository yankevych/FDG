# Generated by Django 3.1.3 on 2020-11-22 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0020_auto_20201122_1605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dataset',
            old_name='file_path',
            new_name='file_name',
        ),
    ]