# Generated by Django 5.0.1 on 2024-01-20 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('STD_App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='roll_number',
        ),
    ]
