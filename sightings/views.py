from django.shortcuts import render, get_object_or_404, redirect
from .models import Sighting
from django.db.models import Count

from .forms import SightingForm

# Create your views here.

def display_sightings(request):
    """Display all sightings in our model"""

    sightings = Sighting.objects.all()
    context = {
            'sightings': sightings,
    }
    return render(request, 'sightings/sightings.html', context)

def edit_sighting(request, sighting_id):
    """View to edit particular sighting"""

    sighting = get_object_or_404(Sighting, pk=sighting_id)
    if request.method == 'POST':
        form = SightingForm(request.POST, instance=sighting)
        if form.is_valid():
            form.save()
            return redirect('/sightings')
    else:
        form = SightingForm(instance=sighting)
    context = {
        'form': form,
    }
    return render(request, 'sightings/edit.html', context)
    
def add_sighting(request): 
    """View to add a sighting"""

    if request.method == 'POST': 
        form = SightingForm(request.POST) 
        if form.is_valid():
            form.save() 
            return redirect('/sightings') 
    else: 
        form = SightingForm() 
    context = { 
        'form': form,
 } 
    return render(request,'sightings/edit.html', context)

def display_stats(request):
    """View to display some statistics on all sightings"""

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
    return render(request, 'sightings/stats.html', context)
