from django.shortcuts import render
from Catch.models import Pet, PetUser, Event
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.views import generic

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
#from .forms import ChangeProfileForm
#from django.contrib.auth.forms import UserChangeForm
# Create your views here.

class EventCreate(CreateView):
    model = Event
    fields = ['name', 'pet', 'location', 'datetime', 'capacity', 'description', 'image', 'duration', 'host']
    #datetime needs to be inputted in this format:
    #1997-04-24 04:41:58

class PetCreate(CreateView):
    model = Pet
    fields = ['name', 'pet_type', 'breed', 'description', 'image', 'owner']

class UserSignUpView(CreateView):
    model = PetUser
    fields = ('username', 'first_name', 'last_name','password','email','location','description')
    template_name = 'sign_up.html'
    success_url = reverse_lazy('homePage')

class BlogCreationView(generic.TemplateView):
    template_name =  'create_blog.html'

    def get(self, request):
        form = BlogCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = BlogCreationForm(request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.author = request.user
            new_blog.save()
            data = form.cleaned_data
            form = BlogCreationForm()
            return redirect('success')
        args = { 'form': form, 'text': data }
        return render(request, self.template_name, args)

def home(request):
    events = Event.objects.all()
    context = {
        "events": events,
    }
    return render(request, 'homePage.html', context = context)

def events(request):
    events = Event.objects.all()
    context = {
        "events": events,
    }
    return render(request, 'eventsPage.html', context = context)

def map(request):
    events = Event.objects.all()
    context = {
        "events": events,
    }
    return render(request, 'mapPage.html', context = context)

def profile(request):
    pets = Pet.objects.all()
    owner = PetUser.objects.filter(username = "ProfileUser")
    context = {
        "pets": pets,
        "owner" : owner,
    }
    return render(request, 'profilePage.html', context = context)

def about(request):
    return render(request, 'aboutPage.html')

# def navbar(request):
#     return render(request, 'events.html')

# def edit_profile(request):
#     pet_user = request.user

#     # If this is a POST request then process the Form data
#     if request.method == 'POST':
#         # Create a form instance and populate it with data from the request (binding):
#         form = ChangeProfileForm(request.POST, instance=pet_user)

#         # Check if the form is valid:
#         if form.is_valid():
#                 # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
#             pet_user.email = form.cleaned_data['email']
#             pet_user.save()
#             form.save()
#                 # redirect to a new URL:
#             return HttpResponseRedirect(reverse('aboutPage') )

#     # If this is a GET (or any other method) create the default form.
#     else:
#         form = ChangeProfileForm()

#         context = {
#             'form': form,
#             'book_instance': pet_user,
#         }
#     return render(request, 'change_profile.html', context)


# When I opened up http://localhost:8000/Catch/profile/edit, filled out the new email, and hit sumbit, nothing happened. The new email was not saved. 
# I fiddled around and found out the it never got inside the first if because request.method!=POST. 