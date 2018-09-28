from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'Catch/homePage.html',)

def about(request):
    return render(request, 'Catch/aboutPage.html')
