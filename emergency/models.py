from django.db import models

class Hospital(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class Ambulance(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, null=True, blank=True, default=None)  # Allow null values
    latitude = models.FloatField()
    longitude = models.FloatField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.hospital.name if self.hospital else 'No Hospital'} - {'Available' if self.available else 'Not Available'}"


from django.db import models

class Patient(models.Model):
    

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    blood_group = models.CharField(
    max_length=5, 
    choices=[
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    ],
    default='O+',  # Provide a default value
)

    contact = models.CharField(max_length=15)
    address = models.TextField()
    medical_history = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
from django.db import models

class EmergencyRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    details = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"
