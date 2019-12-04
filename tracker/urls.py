from django.urls import path

from . import views

urlpatterns = [ 
        path('', views.index, name='index'),
        path('map/', views.coordinates, name='map'),
        path('<int:sighting_id>/', views.detail, name='detail'),
]
