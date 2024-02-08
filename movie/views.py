from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie

# Create your views here.

def home(request):
   # return HttpResponse('<h1>hola homepage</h1>')
   # return render(request, 'home.html')
   # return render(request, 'home.html', {'name': 'Juan Andrés'})
    
    searchTerm = request.GET.get('searchMovie')
    if searchTerm == None:
        movies = Movie.objects.all()
    else:
        movies = Movie.objects.filter(title__contains=searchTerm)
    return render(request, 'home.html', {'searchTerm': searchTerm, 'movies': movies})

def about(request):
    # return HttpResponse('<h1>hola about</h1>')
    return render(request, 'about.html')
