from django.urls import path

from . import views

urlpatterns = [ 
        path('', views.display_sightings, name='sightings'),
        path('<int:sighting_id>', views.edit_sighting, name='edit'),
        path('stats', views.display_stats, name='stats'),
        path('add', views.add_sighting, name='add'),
]
