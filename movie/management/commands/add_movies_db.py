from django.core.management.base import BaseCommand
from movie.models import Movie
import os
import json

class Command(BaseCommand):
    help = 'Load movies from movies.json into the database'

    def handle(self, *args, **kwargs):

        json_file_path = 'movie/management/commands/movies.json'

        with open(json_file_path, 'r') as file:
            data = json.load(file)

        for i in range(100):
            movie = data[i]
            exist = Movie.objects.filter(title=movie['title']).first()
            if not exist:
                Movie.objects.create(
                    title=movie['title'],
                    image='movie/images/default-movie.jpg',
                    genre = movie['genre'],
                    year = movie['year'])