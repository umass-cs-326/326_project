from django.shortcuts import render
from carton.models import Course
from django.views import generic
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse
from .models import Session
from random import choice

# Create your views here.
#class ClassSessionView(generic.DetailView):
#    model = ClassSession
#    template_name = "detail.html"


def calendar(request):
    # sessions describes all of the class sessions that will be displayed by the calendar
    # Expected to store the items as a list with the format:
    # [course name, start time, end time, days of the week] for each session
    sessions = [
        [session.course.name, '{0}:00'.format(i+8), '{0}:00'.format(i+9), choice([[1,3,5],[2,4]])]
        for (i, session)
        in enumerate(Session.objects.all())
    ]
    return render(request, 'main.html', {"sessions": sessions})

def index(request):
    
    template = get_template('index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))