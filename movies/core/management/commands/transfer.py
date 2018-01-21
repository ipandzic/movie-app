import os

from django.core.management.base import BaseCommand

os.path.dirname(os.path.dirname(__file__))


class Command(BaseCommand):
    help = 'Gets data on movies opening this week from Rotten Tomatoes website.'

    def handle(self, *args, **options):
        os.system('python getmovies.py')
