from django.shortcuts import render, get_object_or_404, redirect
from .models import Sighting
from django.db.models import Count

from .forms import SightingForm

# Create your views here.

def sightings(request):
    sightings = Sighting.objects.all()
    context = {
            'sightings': sightings,
    }
    return render(request, 'tracker/sightings.html', context)

def edit_sighting(request, sighting_id):
    sighting = get_object_or_404(Sighting, pk=sighting_id)
    if request.method == 'POST':
        form = SightingForm(request.POST, instance=sighting)
        if form.is_valid():
            form.save()
            return redirect(f'/tracker/sightings')
    else:
        form = SightingForm(instance=sighting)
    context = {
        'form': form,
    }
    return render(request, 'tracker/edit.html', context)
    
def add(request): 
    if request.method == 'POST': 
        form = SightingForm(request.POST) 
        if form.is_valid():
            form.save() 
            return redirect('/tracker/sightings') 
    else: 
        form = SightingForm() 
    context = { 
        'form': form,
 } 
    return render(request,'tracker/edit.html', context)

def coordinates(request):
    # need to choose 100 unique id squirrels
    sightings  = Sighting.objects.all()[:100]
    context = {
            'sightings' : sightings,
    }
    return render(request, 'tracker/map.html', context)


def stats(request):
    sightings_age = Sighting.objects.values('age').order_by('age').annotate(age_count=Count('age'))
    sightings_primary_fur_color = Sighting.objects.values('primary_fur_color').order_by('primary_fur_color').annotate(primaryfurcolor_count=Count('primary_fur_color'))
    sightings_location =  Sighting.objects.values('location').order_by('location').annotate(location_count=Count('location'))
    sightings_running = Sighting.objects.values('running').order_by('running').annotate(running_count=Count('running'))
    sightings_eating = Sighting.objects.values('eating').order_by('eating').annotate(eating_count=Count('eating'))
    context = {
        'sightings_age': sightings_age,
        'sightings_primary_fur_color': sightings_primary_fur_color,
        'sightings_location': sightings_location,
        'sightings_running': sightings_running,
        'sightings_eating': sightings_eating,
    }
    return render(request, 'tracker/stats.html', context)
