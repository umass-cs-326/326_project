from django.shortcuts import render
from Catch.models import Pet, PetUser, Event
from django.views.generic.edit import CreateView
from django.http import HttpResponse
# Create your views here.

class EventCreate(CreateView):
    model = Event
    fields = ['name', 'pet', 'location', 'datetime', 'capacity', 'description', 'image', 'duration', 'host']
    #datetime needs to be inputted in this format:
    #1997-04-24 04:41:58

class PetCreate(CreateView):
    model = Pet
    fields = ['name', 'pet_type', 'breed', 'description', 'image', 'owner']


def home(request):
    events = Event.objects.all()
    context = {
        "events": events,
    }
    return render(request, 'homePage.html', context = context)

def events(request):
    events = Event.objects.all()
    context = {
        "events": events,
    }
    return render(request, 'eventsPage.html', context = context)

def map(request):
    events = Event.objects.all()
    context = {
        "events": events,
    }
    return render(request, 'mapPage.html', context = context)

def profile(request):
    pets = Pet.objects.all()
    owner = PetUser.objects.filter(username = "ProfileUser")
    context = {
        "pets": pets,
        "owner" : owner,
    }
    return render(request, 'profilePage.html', context = context)

def about(request):
    return render(request, 'aboutPage.html')

# def navbar(request):
#     return render(request, 'events.html')
