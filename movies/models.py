from django.db import models

# Create your models here.
# Easily changed on Admin page but also has script to get data from .csv
class Movie(models.Model):
    title = models.CharField(max_length=200)
    movie_poster_image = models.ImageField(blank=True, null=True,
		upload_to="posters/")
    release_date = models.DateField()
    director = models.CharField(max_length=200)
    rating = models.CharField(max_length=10)
    genre = models.CharField(max_length=50)
    description = models.TextField()
	
    def __str__(self):
        return "%s" % (self.title)

# Has script to populate data from .csv
class Seat(models.Model):
    #row = models.SmallIntegerField()
    #seat_num = models.SmallIntegerField()
    seat_label = models.CharField(max_length=4)
    available = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % (self.seat_label)

#Has script to populate data and add to .json file
class Auditorium(models.Model):
    #seat_id = models.ForeignKey(Seat, on_delete=models.CASCADE)
    auditorium_name = models.CharField(max_length=100)
    
    def __str__(self):
        return "%s" % (self.auditorium_name)

#Has script to populate data but has to be changed if ForeignKeys in
#Auditorium or Seat Models change
class AuditoriumSeat(models.Model):
    auditorium_id = models.ForeignKey(Auditorium, on_delete=models.CASCADE)
    seat_id = models.ForeignKey(Seat, on_delete=models.CASCADE)

# Easily changed on Admin page, no script
class MovieTime(models.Model):
    movie_time = models.TimeField()

    def __str__(self):
        return "%s" % (self.movie_time)

# Easily changed on Admin page, no script
class Screening(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    auditorium = models.ForeignKey(Auditorium, on_delete=models.CASCADE)
    start_time = models.ForeignKey(MovieTime, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.movie, self.start_time)

# Easily changed on Admin page but, also has script to read from .csv file
class Price(models.Model):
    type =  models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return "%s" % (self.type)


class Ticket(models.Model):
    screening_id = models.ForeignKey(Screening, on_delete=models.CASCADE)
    seat_id = models.ForeignKey(Seat, on_delete=models.CASCADE, default = 1)
    price = models.ForeignKey(Price, models.DO_NOTHING, blank = True)
    #choice = models.CharField(default = "0", max_length = 200)
    #payment_id = ForeignKey(Payment, on_delete=models.CASCADE)
    #paid = models.BooleanField()
    #reserved = models.BooleanField()
