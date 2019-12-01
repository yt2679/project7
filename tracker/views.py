from django.shortcuts import render
from .models import Sighting




# Create your views here.

def sightings(request):
    all_squirrels = Sighting.objects.all()
    return render(request, 'tracker/sightings.html', locals())


