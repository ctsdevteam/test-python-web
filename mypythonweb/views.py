from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    ##return HttpResponse("Welcome to the home page")
    context = {
        'title': 'Home page',
    }
    return render(request, 'home-page.html', context)

def about(request):
    ##return HttpResponse("This is the about page")
    context = {
        'title': 'About page',
    }
    return render(request, 'about-page.html', context)