from django.shortcuts import render
from Catch.models import Pet, PetUser, Event

# Create your views here.
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
    owner = PetUser.objects.filter(username = "ProfileUser")
    pets = Pet.objects.all()
    context = {
        "pets": pets,
        "owner" : owner,
    }
    return render(request, 'profilePage.html', context = context)

def about(request):
    return render(request, 'aboutPage.html')

# def navbar(request):
#     return render(request, 'events.html')
