from django.shortcuts import render
from classdoor.models import Course, Teacher, Review, University, User, Subject

# Create your views here.
def index(request):
    return render(request, "index.html")

def classpage(request, name):
    data = Course.objects.all()
    print(data)
    return render(request, "class.html", {'data':data})

def feed(request):
    return render(request, "feed.html")

def login(request):
    return render(request, "login.html")

def profile(request):
    return render(request, "profile.html")

def review(request):
    return render(request, "WriteReviewTemplate.html")