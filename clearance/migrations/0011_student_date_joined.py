# Generated by Django 4.2.15 on 2024-08-22 10:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clearance', '0010_remove_student_department_clearance'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
