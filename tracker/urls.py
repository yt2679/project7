from django.urls import path

from . import views

urlpatterns = [ 
        # maybe should add index so that tracker/ displays something
        path('sightings', views.sightings, name='sightings'),
        path('map', views.coordinates, name='map'),
        path('sightings/<int:sighting_id>', views.edit_sighting, name='edit'),
        path('sightings/<int:sighting_id>/delete', views.delete, name='delete'),
        path('sightings/stats', views.stats, name='stats'),
        path('sightings/add', views.add, name='add'),
]
