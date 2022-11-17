# Generated by Django 4.1.3 on 2022-11-16 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('EmpManager', '0002_delete_employeerecord'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.IntegerField(default=0)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('contact', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=20)),
                ('salary', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='media')),
            ],
        ),
    ]
