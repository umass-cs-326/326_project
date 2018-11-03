import re
from django.shortcuts import render
from classdoor.models import Course, Teacher, Review, University, User, Subject

# Create your views here.
def index(request):
    return render(request, "index.html")

def classpage(request, id):
    # Get the individual course by id from url
    course = Course.objects.get(pk=id)

    courseData = {}
    courseData["class"] = course
    courseData["name"] = course.name
    courseData["description"] = course.description
    courseData["teacher"] = course.teacher
    courseData["star_rating"] = course.starRating
    courseData["reviews"] = course.reviews
    courseData["average_grade"] = course.averageGrade
    courseData["subject"] = course.subject
    courseData["universityName"] = course.university_name

    # Get all the reviews for the course
    reviews = course.reviews.all()

    reviewList = []

    # Get the information about all the individual reviews in the list
    for rdata in reviews:
        reviewData = {}
        reviewData["review"] = rdata
        reviewData["title"] = rdata.title
        reviewData["text"] = rdata.text
        reviewData["star_rating"] = rdata.starRating
        reviewData["grade_received"] = rdata.gradeReceived
        reviewData["date"] = rdata.date
        reviewData["tags"] = rdata.tags
        reviewData["author"] = rdata.author

        reviewList.append(reviewData)

    # Add to course information and the list of reviews to the page context
    context = {
        "class": courseData,
        "review_list": reviewList,
    }

    return render(request, "class.html", context=context)

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
    return render(request, "profile.html")

def review(request):
    return render(request, "WriteReviewTemplate.html")