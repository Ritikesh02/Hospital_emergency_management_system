# Generated by Django 4.2.20 on 2025-03-28 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emergency', '0002_alter_ambulance_hospital'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10)),
                ('contact', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('medical_history', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
