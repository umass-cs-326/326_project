from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from .models import Events

class EventsCreate(CreateView):
    model = Events
    fields = ['event_name', 'event_description', 'event_capacity']




def home(request):
    return render(request, 'Catch/homePage.html',)

def events(request):
    # list_events = Events.objects.filter(event_name__exact="Cathys Cat Emporium")
    eventList = Events.objects.all()
    context = {'Events': eventList}
    return render(request, 'Catch/eventsPage.html', context)

def profile(request):
    return render(request, 'Catch/profilePage.html')

def form(request):
    return render(request, 'Catch/Events_form.html')

def map(request):
    return render(request, 'Catch/mapPage.html',)

def about(request):
    return render(request, 'Catch/aboutPage.html')

def navbar(request):
    return render(request, 'Catch/events.html')
