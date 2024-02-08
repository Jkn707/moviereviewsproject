from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
   # return HttpResponse('<h1>hola homepage</h1>')
   # return render(request, 'home.html')
    return render(request, 'home.html', {'name': 'Juan Andrés'})

def about(request):
    # return HttpResponse('<h1>hola about</h1>')
    return render(request, 'about.html')
