from movies.models import Price
from django.core.management.base import BaseCommand

from csv import DictReader

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the pet data from the CSV file,
first destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from prices.csv into our Price model"

    def handle(self, *args, **options):
        if Price.objects.exists():
            print('Price data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Creating price data")
        for row in DictReader(open('./prices.csv')):
            price = Price()
            price.type = row['Type']
            price.price = row['Price']
            price.save()
