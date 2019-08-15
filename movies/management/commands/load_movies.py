from movies.models import Movie
from django.core.management.base import BaseCommand

from csv import DictReader


ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""

class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from movies.csv into our Movie model"

    def handle(self, *args, **options):
        if Movie.objects.exists():
            print('Movie data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Creating movie data")
        for row in DictReader(open('./movies.csv')):
            movie = Movie()
            movie.title = row['Title']
            #movie.movie_poster_image = models.ImageField(blank=True, null=True,
            #upload_to="posters/")
            movie.release_date = row['Release_date']
            movie.director = row['Director']
            movie.rating = row['Rating']
            movie.genre = row['Genre']
            movie.description = row['Description']
            movie.save()
