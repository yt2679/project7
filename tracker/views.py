from django.shortcuts import render
from .models import Sighting




# Create your views here.

def sightings(request):
    sightings = Sighting.objects.all()
    context = {
            'sightings': sightings,
    }
    return render(request, 'tracker/sightings.html', context)

def coordinates(request):
    cooridnates  = Sighting.objects.all()[:100]
    context = {
            'coordinates' : coordinates,
    }
    return render(request, 'tracker/map.html', context)

