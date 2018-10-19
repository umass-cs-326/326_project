from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from .models import Events, Pet

class EventsCreate(CreateView):
    model = Events
    fields = ['event_name', 'event_description', 'event_capacity']


class PetCreate(CreateView):
    model = Pet
    fields = ['pet_name', 'pet_age', 'pet_description', 'pet_breed']

def home(request):
    eventList = Events.objects.all()
    context = {'Events': eventList}
    return render(request, 'Catch/homePage.html', context)

def events(request):
    # list_events = Events.objects.filter(event_name__exact="Cathys Cat Emporium")
    eventList = Events.objects.all()
    context = {'Events': eventList}
    return render(request, 'Catch/eventsPage.html', context)

def profile(request):
    petList = Pet.objects.all()
    context = {'Pets': petList}
    return render(request, 'Catch/profilePage.html', context)

def form(request):
    return render(request, 'Catch/Events_form.html')

def map(request):
    return render(request, 'Catch/mapPage.html',)

def about(request):
    return render(request, 'Catch/aboutPage.html')

def navbar(request):
    return render(request, 'Catch/events.html')
