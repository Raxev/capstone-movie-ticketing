from django.conf.urls import url
# gets views from current directory
from . import views
from django.urls import path

# allows Django to know which app is using a variable name if variable
# names are the same
app_name = 'movies'

urlpatterns = [
    #/movies/
    url(r'^$', views.index, name='index'),

    #/movies/275/
    url(r'^(?P<movie_id>[0-9]+)/$',views.movie_detail, name = 'movie_detail'),
    url(r'^movies/contact_us$', views.contact_us, name = 'contact_us'),
    url(r'^movies/about_us$', views.about_us, name = 'about_us'),
	url(r'^movies/promotions$', views.promotions, name = 'promotions'),
	url(r'^movies/menu$', views.menu, name='menu'),
	url(r'^movies/ticket_sale$', views.ticket_sale, name = 'ticket_sale'),
	url(r'^movies/reservation_confirm$', views.reservation_confirm, name = 'reservation_confirm'),
    # path('<int:pk>/ticket/', views.TicketView.as_view(), name='ticket'),
    # path('<int:movie_id>/buy/', views.buy, name = 'buy'),
    	
]
