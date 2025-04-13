from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import requests
from geopy.distance import geodesic
from .models import Ambulance, Hospital

from django.http import JsonResponse

def nearest_ambulance(request):
    # Example: Return a dummy response for nearest ambulance
    data = {
        "ambulance": {
            "lat": 31.2232, # Dummy latitude (change to real data)
            "lon": 75.7670,  # Dummy longitude (change to real data)
            "eta": 10  # Example ETA in minutes
        }
    }
    return JsonResponse(data)


from django.shortcuts import render

def request_help(request):
    # Automatically show "Call an Ambulance" button when page loads
    return render(request, 'emergency/request_help.html', {'submitted': True})


import requests
from django.http import JsonResponse
from geopy.distance import geodesic

def hospitals_list(request):
    """Render the hospital list page."""
    auto_detect = request.GET.get('auto_detect', 'false') == 'true'
    return render(request, 'emergency/hospitals_list.html', {'auto_detect': auto_detect})

def nearby_hospitals(request):
    """Fetch hospitals and clinics dynamically based on the user's actual location."""
    lat = request.GET.get("lat")
    lon = request.GET.get("lon")

    if not lat or not lon:
        return JsonResponse({"error": "Latitude and longitude are required."}, status=400)

    try:
        user_location = (float(lat), float(lon))
    except ValueError:
        return JsonResponse({"error": "Latitude and longitude must be valid numbers."}, status=400)

    overpass_url = "http://overpass-api.de/api/interpreter"
    overpass_query = f"""
    [out:json];
    (
      node["amenity"="hospital"](around:10000,{lat},{lon});
      node["amenity"="clinic"](around:10000,{lat},{lon});
    );
    out body;
    """

    try:
        response = requests.get(overpass_url, params={'data': overpass_query})
        response.raise_for_status()
        data = response.json().get('elements', [])

        hospitals = []
        for place in data:
            tags = place.get('tags', {})
            name = tags.get('name', '').strip()
            if not name:
                continue  

            address = (
                tags.get('addr:full')
                or tags.get('addr:street')
                or tags.get('addr:city')
                or "Address Not Available"
            )

            place_lat = place.get('lat')
            place_lon = place.get('lon')
            if not place_lat or not place_lon:
                continue  

            distance = geodesic(user_location, (place_lat, place_lon)).km  

            hospitals.append({
                'name': name,
                'address': address,
                'distance': round(distance, 2),
                'lat': place_lat,
                'lon': place_lon
            })

        # Sort by nearest hospitals and return the top 20 closest
        hospitals = sorted(hospitals, key=lambda x: x['distance'])[:20]

        return JsonResponse({'hospitals': hospitals})

    except requests.exceptions.RequestException:
        return JsonResponse({"error": "Failed to fetch hospitals. Try again later."}, status=500)




from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient
from .forms import PatientForm

# View for listing patients and adding new ones
def patients_details(request):
    patients = Patient.objects.all()
    form = PatientForm()

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patients_details')

    return render(request, 'emergency/patients_details.html', {'form': form, 'patients': patients})

# View for editing patient details
def edit_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patients_details')
    else:
        form = PatientForm(instance=patient)

    return render(request, 'emergency/edit_patient.html', {'form': form, 'patient': patient})

# View for deleting a patient
def delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        patient.delete()
        return redirect('patients_details')

    return render(request, 'emergency/delete_patient.html', {'patient': patient})


from django.shortcuts import render

def home_view(request):
    return render(request, "home.html")  # Ensure this matches the correct path
from django.shortcuts import render