# Generated by Django 3.1.3 on 2020-11-21 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('administrator', '0005_auto_20201121_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schema',
            name='creator',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]