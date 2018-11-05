from django.shortcuts import render
from carton.models import Course
from django.views import generic
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse
from .models import Session

# Create your views here.
#class ClassSessionView(generic.DetailView):
#    model = ClassSession
#    template_name = "detail.html"


def calendar(request):
    
    # template = get_template('main.html')
    # context = {
    # }
    sessions = [
        [session.course.name, '{0}:00'.format(i+1), '{0}:00'.format(i+2), [1,3,5]]
        for (i, session)
        in enumerate(Session.objects.all())
    ]
    return render(request, 'main.html', {"sessions": sessions})
    # return HttpResponse(template.render(context, request))
    
def index(request):
    
    template = get_template('index.html')
    context = {
    }
    return HttpResponse(template.render(context, request))