from django.core.management.base import BaseCommand
import pandas as pd
from tracker.models import Sighting

class Command(BaseCommand):
    help = 'imports squirrel data from path'
    
    def add_arguments(self, parser):
        parser.add_argument('path', type=str)
    
    def handle(self, *args, **kwargs):
        path = kwargs['path']
        df = pd.read_csv(path)
        for index, row in df.iterrows():
            sighting = Sighting()
            sighting.latitude = row['Y']
            sighting.longitude = row['X']
            sighting.unique_squirrel_id = row['Unique Squirrel ID']
            sighting.shift = row['Shift']
            date = str(row['Date'])
            sighting.date = f'{date[4:]}-{date[:2]}-{date[2:4]}'
            sighting.age = row['Age']
            sighting.primary_fur_color = row['Primary Fur Color']
            sighting.location = row['Location']
            sighting.specific_location = row['Specific Location']
            sighting.running = row['Running']
            sighting.chasing = row['Chasing']
            sighting.climbing = row['Climbing']
            sighting.eating = row['Eating']
            sighting.foraging = row['Foraging']
            sighting.other_activities = row['Other Activities']
            sighting.kuks = row['Kuks']
            sighting.quaas = row['Quaas']
            sighting.moans = row['Moans']
            sighting.tail_flags = row['Tail flags']
            sighting.tail_twitches = row['Tail twitches']
            sighting.approaches = row['Approaches']
            sighting.indifferent = row['Indifferent']
            sighting.runs_from = row['Runs from']
            sighting.save()
