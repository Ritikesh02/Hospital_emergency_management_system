# Generated by Django 4.2.20 on 2025-03-28 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical_records', '0002_remove_medicalrecord_uploaded_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalrecord',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='medical_records/'),
        ),
    ]
