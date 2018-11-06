from django.shortcuts import render
from carton.models import Course, Instructor, Session
from django.views import generic
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse
from .models import Session
from random import choice

# Keeps track of the mapping from letter to number
letters = {
    'm': 1,
    't': 2,
    'w': 3,
    'r': 4,
    'f': 5
}
# The opposite
reverse_letters = {v:k for (k, v) in letters.items()}

def convert_dow_to_list(dow):
    return [letters.get(day) for day in dow if day in letters.keys()]

def convert_dow_to_str(dow):
    return ''.join(reverse_letters.get(day, '') for day in dow)

def calendar(request):
    # sessions describes all of the class sessions that will be displayed by the calendar
    # Expected to store the items as a list with the format:
    # [course name, start time, end time, days of the week] for each session
    session = None
    sessions = [
        [session.course.name, session.start_time.strftime('%H:%M'), session.end_time.strftime('%H:%M'),
         convert_dow_to_list(session.dow)]
        for session
        in Session.objects.all()
    ]
    return render(request, 'main.html', {"sessions": sessions})

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
