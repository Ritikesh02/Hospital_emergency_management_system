from django.urls import path
from .views import (
    request_help,
    nearby_hospitals, 
    hospitals_list, 
    nearest_ambulance,
    patients_details,
    edit_patient,
    delete_patient,
)

urlpatterns = [
    path('nearest-ambulance/', nearest_ambulance, name='nearest_ambulance'),
    path('hospitals-list/', hospitals_list, name='hospitals_list'),
    path('nearby-hospitals/', nearby_hospitals, name='nearby_hospitals'),
    path('request-help/', request_help, name='request_help'),
    path('patients-details/', patients_details, name='patients_details'), 
    path('edit-patient/<int:patient_id>/', edit_patient, name='edit_patient'),
    path('delete-patient/<int:patient_id>/', delete_patient, name='delete_patient'),
]
