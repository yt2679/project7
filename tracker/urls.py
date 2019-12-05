from django.urls import path

from . import views

urlpatterns = [ 
        path('sightings', views.sightings, name='sightings'),
        path('map', views.coordinates, name='map'),
        path('sightings/<int:sighting_id>', views.edit_sighting, name='edit'),
        path('sightings/stats', views.stats, name='stats'),
        path('sightings/add', views.add, name='add'),
]
