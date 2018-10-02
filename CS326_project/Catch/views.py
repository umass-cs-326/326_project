from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Catch/homePage.html',)

def events(request):
    return render(request, 'Catch/eventsPage.html')

def map(request):
    return render(request, 'Catch/mapPage.html',)

def profile(request):
    return render(request, 'Catch/profilePage.html')

def about(request):
    return render(request, 'Catch/aboutPage.html')

def navbar(request):
    return render(request, 'Catch/events.html')
