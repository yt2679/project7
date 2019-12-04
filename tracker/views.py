from django.shortcuts import render, get_object_or_404, redirect
from .models import Sighting


# Create your views here.

def sightings(request):
    sightings = Sighting.objects.all()
    context = {
            'sightings': sightings,
    }
    return render(request, 'tracker/sightings.html', context)

def detail(request, sighting_id):
    sighting = get_object_or_404(Sighting, pk=sighting_id)
    context = {
            'sighting': sighting
    }
    return render(request, 'tracker/detail.html', context)


def coordinates(request):
    # need to choose 100 unique id squirrels
    sightings  = Sighting.objects.all()[:100]
    context = {
            'sightings' : sightings,
    }
    return render(request, 'tracker/map.html', context)

def delete(request, sighting_id):
    sighting = get_object_or_404(Sighting, pk=sighting_id)
    if request.method == 'POST':
        sighting.delete()
        return redirect('/tracker/sightings')
    return render(request, 'tracker/detail.html', {'sighting': sighting})
