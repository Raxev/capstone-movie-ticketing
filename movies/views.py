# from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from . forms import ContactForm


from .models import Movie, AuditoriumSeat, Screening, Auditorium, MovieTime, Ticket, Price

# Create your views here.
def index(request):
    all_movies = Movie.objects.all()

    # info template needs
    context = {'all_movies': all_movies}
    return render(request, 'movies/index.html', context)


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            context = { 'movie': movie, 
						'name': form.cleaned_data['name'], 
						'email': form.cleaned_data['email'] ,
						'num_child': form.cleaned_data['num_child'] ,
						'num_adult': form.cleaned_data['num_adult'] ,
						'num_senior': form.cleaned_data['num_senior'] ,
						'num_student': form.cleaned_data['num_student'] ,
						'num_matinee': form.cleaned_data['num_matinee'],
						'total': form.total(),
						} 
            return render(request, 'movies/ticket_sale.html',  context)
    else:
        form = ContactForm()
    
    return render(request, 'movies/movie_detail.html', {'movie': movie, 'prices': Price.objects.all(), 'form': form})
    
def menu(request):
    return render(request, 'movies/menu.html', )

def contact_us(request):
    return render(request, 'movies/contact_us.html', )

def about_us(request):
    return render(request, 'movies/about_us.html')
	
def promotions(request):
	return render(request, 'movies/promotions.html')

def ticket_sale(request):
    return render(request, 'movies/ticket_sale.html')
    
def reservation_confirm(request):
	return render(request, 'movies/reservation_confirm.html')
    
    
class TicketView(generic.DetailView):

    model = Movie
    
    template_name = 'movies/movies_auditorium.html'
    
    def get_context_data(self,**kwargs):
        
        context = super(TicketView, self).get_context_data(**kwargs)
        
        movie_pk = self.kwargs.get('pk')
        scr = Screening.objects.filter(movie_id = movie_pk).get()
        context['auditorium'] = Auditorium.objects.filter(pk=scr.auditorium_id).get()
        context['movie_time'] = MovieTime.objects.filter(pk=scr.start_time_id).get()
        context['prices'] = Price.objects.all()
        return context
        
    
def buy(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    print(movie_id)
    # selected_choice.votes += 1
    # selected_choice.save()
    return HttpResponseRedirect(reverse('movies:tickets', args=(movie.id,)))        
    
    
