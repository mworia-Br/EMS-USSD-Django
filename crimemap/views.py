from django.shortcuts import render

# Create your views here.
from django.contrib.gis.geos import Point
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
            'coordinates': crime.coordinates.coords
        })

    return render(request, 'crime_map.html', {'crime_data': crime_data})
