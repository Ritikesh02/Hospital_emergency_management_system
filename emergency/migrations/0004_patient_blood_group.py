# Generated by Django 4.2.20 on 2025-03-28 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emergency', '0003_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], default='O+', max_length=5),
        ),
    ]
