# Generated by Django 4.2.1 on 2023-06-09 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seminar', '0009_upisi_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predmeti',
            name='nositelj',
            field=models.ForeignKey(limit_choices_to={'uloga__naziv': 'prof'}, on_delete=django.db.models.deletion.CASCADE, related_name='profesor', to=settings.AUTH_USER_MODEL),
        ),
    ]
