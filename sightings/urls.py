from django.urls import path

from . import views

urlpatterns = [ 
        path('', views.sightings, name='sightings'),
        path('map', views.coordinates, name='map'),
        path('<int:sighting_id>', views.edit_sighting, name='edit'),
        path('stats', views.stats, name='stats'),
        path('add', views.add, name='add'),
]
