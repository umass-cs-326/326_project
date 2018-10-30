from django.shortcuts import render
from carton.models import Class
from django.views import generic

# Create your views here.
class ClassSessionView(generic.DetailView):
    model = ClassSession
    template_name = "detail.html"
