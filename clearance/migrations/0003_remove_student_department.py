# Generated by Django 4.2.15 on 2024-08-21 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clearance', '0002_seed_departments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='department',
        ),
    ]
