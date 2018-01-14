from django.core.management.base import BaseCommand

import os
os.path.dirname(os.path.dirname(__file__))


class Command(BaseCommand):
    help = 'Gets movies from Rotten Tomatoes website'

    def handle(self, *args, **options):
        os.system('python getmovies.py')
