from django.core.management.base import BaseCommand
import pandas as pd

class Command(BaseCommand):
    help = 'imports squirrel data form path'
    
    def add_arguments(self, parser):
        parser.add_argument('n', type=int)
    
    def handle(self, *args, **kwargs):
        n = kwargs['n']
        for i in range(n):
            self.stdout.write(f'{i}')
