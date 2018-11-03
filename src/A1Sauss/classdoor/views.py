from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def classpage(request):
    return render(request, "class.html")

def feed(request):
    
    return render(request, "feed.html", context=data)

def login(request):
    return render(request, "login.html")

def profile(request):
    return render(request, "profile.html")

def review(request):
    return render(request, "WriteReviewTemplate.html")