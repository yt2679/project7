from django.db import models

class Sighting(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    unique_squirrel_id = models.CharField(max_length=100)
    shift = models.CharField(max_length=20)
    date = models.DateField()
    age = models.CharField(max_length=20)
    primary_fur_color = models.CharField(max_length=200)
    location  = models.CharField(max_length=200)
    specific_location  = models.CharField(max_length=200)
    running = models.BooleanField()
    chasing = models.BooleanField()
    climbing = models.BooleanField()
    eating = models.BooleanField()
    foraging = models.BooleanField()
    other_activities = models.CharField(max_length=200)
    kuks = models.BooleanField()
    quaas = models.BooleanField()
    moans = models.BooleanField()
    tail_flags = models.BooleanField()
    tail_twitches = models.BooleanField()
    approaches = models.BooleanField()
    indifferent = models.BooleanField()
    runs_from = models.BooleanField()


