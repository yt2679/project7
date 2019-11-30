from django.core.management.base import BaseCommand
import pandas as pd
from django.utils import timezone

class Command(BaseCommand):
    help = 'imports squirrel data form path'
    
    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write(f'It\'s now {time}')
        
