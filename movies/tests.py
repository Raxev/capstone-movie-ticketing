# from django.test import TestCa
from movies.models import Movie

from django.db import connection


cursor = connection.cursor()

cursor.execute('''select * from Movie where title="Green Book"''')