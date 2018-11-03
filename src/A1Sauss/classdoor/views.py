from django.shortcuts import render
from classdoor.models import Course, Teacher, Review, University, User, Subject

# Create your views here.
def index(request):
    return render(request, "index.html")

def classpage(request):
    return render(request, "class.html")

def feed(request):
    return render(request, "feed.html")

def login(request):
    return render(request, "login.html")

def profile(request):
    return render(request, "profile.html")

def review(request, id):

    course_object = Course.objects.get(pk=id)
    course_name = course_object.name

    context = {
        "course_name": course_name,
    }
    return render(request, "WriteReviewTemplate.html", context = context)