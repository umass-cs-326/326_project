import re

from django.shortcuts import render
from classdoor.models import Course, Teacher, Review, University, User, Subject

# Create your views here.
def index(request):
    return render(request, "index.html")

def classpage(request):
    return render(request, "class.html")

def feed(request):
    context = {}

    courses = Course.objects.all()
    coursesArr = []

    for course in courses:
        courseData = {}

        numIndex = re.search("\d", course.name)

        courseData["class"] = course
        courseData["subject"] = course.name[0: numIndex.start()]
        courseData["number"] = course.name[numIndex.start(): len(course.name)]
        courseData["description"] = course.description
        courseData["star_rating"] = course.starRating

        review = course.reviews.all().first()

        if review:
            courseData["featured_title"] = review.title
            courseData["featured_text"] = review.text

        coursesArr.append(courseData)

    context["course_data"] = coursesArr

    return render(request, "feed.html", context=context)

def login(request):
    return render(request, "login.html")

def profile(request):
	courses = Course.objects.all()[:3]
	reviews = Review.objects.all()[:3]
	
	context = {"reviews": reviews, "courses": courses}
	return render(request, "profile.html", context=context)

def review(request, id):

    course_object = Course.objects.get(pk=id)
    course_name = course_object.name

    context = {
        "course_name": course_name,
    }
    return render(request, "WriteReviewTemplate.html", context = context)
