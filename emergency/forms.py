from django import forms
from .models import Patient, EmergencyRequest  # Combine model imports

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'gender', 'blood_group', 'contact', 'address', 'medical_history']

class EmergencyRequestForm(forms.ModelForm):
    class Meta:
        model = EmergencyRequest
        fields = ['name', 'phone', 'details']
