# Generated by Django 4.2.1 on 2023-06-03 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seminar', '0006_user_is_admin_user_is_student_user_is_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_student',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_teacher',
        ),
    ]
