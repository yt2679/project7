from django.shortcuts import render
from .models import Sighting




# Create your views here.

def sightings(request):
    sightings = Sighting.objects.all()
    context = {
            'sightings': sightings,
    }
    return render(request, 'tracker/sightings.html', context)


