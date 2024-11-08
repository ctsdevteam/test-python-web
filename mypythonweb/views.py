from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    ##return HttpResponse("Welcome to the home page")
    context = {
        'title': 'Welcome to Our Website!',
    }
    return render(request, 'home.html', context)

def about(request):
    return HttpResponse("This is the about page")