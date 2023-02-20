from django.shortcuts import render

# Create your views here.
from .models import Crime

def crime_map(request):
    crimes = Crime.objects.all()
    crime_data = []
    for crime in crimes:
        crime_data.append({
            'date': crime.date,
            'time': crime.time,
            'location': crime.location,
            'description': crime.description,
            'longitude': crime.longitude,
            'latitude': crime.latitude,
        })

    return render(request, 'crime_map.html', {'crime_data': crime_data})
