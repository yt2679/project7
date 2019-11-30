from django.core.management.base import BaseCommand
import pandas as pd

class Command(BaseCommand):
    help = 'imports squirrel data form path'
    
    def add_arguments(self, parser):
        parser.add_argument('path', type=str)
    
    def handle(self, *args, **kwargs):
        path = kwargs['path']
        df = pd.read_csv(path)
        print(df)
