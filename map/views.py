from django.shortcuts import render
from sightings.models import Sighting

# Create your views here.

def display_map(request):
    """View to display map of 100 sightings"""

    sightings = Sighting.objects.all()[:100]
    context = {
            'sightings' : sightings,
    }
    return render(request, 'map/map.html', context)
