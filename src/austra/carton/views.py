from django.shortcuts import render
from carton.models import Course, Instructor, Session
from django.views import generic
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse


def calendar(request):
    
    template = get_template('main.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
    
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