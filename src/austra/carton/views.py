from django.shortcuts import render
from carton.models import Class
from django.views import generic

# Create your views here.
class ClassInstanceView(generic.DetailView):
    model = ClassInstance
    template_name = "main.html"
