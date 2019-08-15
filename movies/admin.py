from django.contrib import admin
# Model is in the same folder
from .models import Movie, Price, Auditorium, AuditoriumSeat, MovieTime, Screening, Ticket

# Register your models here.
admin.site.register(Movie)
admin.site.register(Price)
admin.site.register(Auditorium)
admin.site.register(AuditoriumSeat)
admin.site.register(MovieTime)
admin.site.register(Screening)
admin.site.register(Ticket)