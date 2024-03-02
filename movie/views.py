from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie

import matplotlib.pyplot as plt
import matplotlib
import io
import urllib, base64

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

def yearstatistics_view(request):
    matplotlib.use('Agg')

    all_movies = Movie.objects.all()

    movie_count_by_genre = {}

    for movie in all_movies:
        year = movie.year if movie.year else "None"

        if year in movie_count_by_genre:
            movie_count_by_genre[year] += 1
        else:
            movie_count_by_genre[year] = 1


    bar_width = 0.5

    year_bar_positions = range(len(movie_count_by_genre))


    plt.bar(year_bar_positions, movie_count_by_genre.values(), width=bar_width)

    plt.title('Movies by year')
    plt.xlabel('Year')
    plt.ylabel('Movies')
    plt.xticks(year_bar_positions, movie_count_by_genre.keys(), rotation = 90)

    plt.subplots_adjust(bottom=0.3)

    yearPlot = io.BytesIO()

    plt.savefig(yearPlot, format='png')
    yearPlot.seek(0)
    plt.close()

    yearPlot_png = yearPlot.getvalue()
    yearPlot.close()

    yeargraphic = base64.b64encode(yearPlot_png)
    yeargraphic = yeargraphic.decode('utf-8')


    return render(request, 'yearstatistics.html', {'yeargraphic': yeargraphic})

def genrestatistics_view(request):
    matplotlib.use('Agg')

    all_movies = Movie.objects.all()

    movie_count_by_genre = {}

    for movie in all_movies:
        genre = movie.genre[0] if movie.genre[0] else "None"

        if genre in movie_count_by_genre:
            movie_count_by_genre[genre] += 1
        else:
            movie_count_by_genre[genre] = 1


    bar_width = 0.5

    genre_bar_positions = range(len(movie_count_by_genre))


    plt.bar(genre_bar_positions, movie_count_by_genre.values(), width=bar_width)

    plt.title('Movies by genre')
    plt.xlabel('Genre')
    plt.ylabel('Movies')
    plt.xticks(genre_bar_positions, movie_count_by_genre.keys(), rotation = 90)

    plt.subplots_adjust(bottom=0.3)

    genrePlot = io.BytesIO()

    plt.savefig(genrePlot, format='png')
    genrePlot.seek(0)
    plt.close()

    genrePlot_png = genrePlot.getvalue()
    genrePlot.close()

    genregraphic = base64.b64encode(genrePlot_png)
    genregraphic = genregraphic.decode('utf-8')


    return render(request, 'genrestatistics.html', {'genregraphic': genregraphic})