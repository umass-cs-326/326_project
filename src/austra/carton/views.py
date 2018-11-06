from django.shortcuts import render
from carton.models import Course, Instructor, Session
from django.views import generic
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse
from .models import Session
from random import choice


def calendar(request):
    # sessions describes all of the class sessions that will be displayed by the calendar
    # Expected to store the items as a list with the format:
    # [course name, start time, end time, days of the week] for each session
    sessions = [
        [session.course.name, '{0}:00'.format(i+8), '{0}:00'.format(i+9), choice([[1,3,5],[2,4]])]
        for (i, session)
        in enumerate(Session.objects.all())
    ]
    courses = [
        [course.name, course.rating, course.session_set.all(), course.id]
        for (i, course)
        in enumerate(Course.objects.all())
    ]
    return render(request, 'main.html', {"sessions": sessions, "courses": courses})

def index(request):
    
    template = get_template('index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

class InstructorListView(generic.ListView):
    model = Instructor
    template_name = "instructor_list.html"

class InstructorDetailView(generic.DetailView):
    model = Instructor
    template_name = "instructor_detail.html"

