# Generated by Django 4.1.3 on 2022-11-16 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EmpManager', '0004_rename_image_employeerecord_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeerecord',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='employeerecord',
            name='gender',
        ),
    ]
