from django.db import models
from django.utils.timezone import now

class MedicalRecord(models.Model):
    patient_name = models.CharField(max_length=100)
    description = models.TextField()
    
    file = models.FileField(upload_to="medical_records/", blank=True, null=True)

    upload_date = models.DateTimeField(default=now)  

    def __str__(self):
        return self.patient_name
