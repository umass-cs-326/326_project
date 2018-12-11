from django.shortcuts import render, redirect
from Catch.models import Pet, PetUser, Event
from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.views import generic

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import PetCreationForm
#from django.contrib.auth.forms import UserChangeForm
# Create your views here.

class EventCreate(CreateView):
    model = Event
    fields = ['name', 'pet', 'location', 'datetime', 'capacity', 'description', 'image', 'duration', 'host']
    #datetime needs to be inputted in this format:
    #1997-04-24 04:41:58

class PetCreate(generic.TemplateView):
    template_name =  'Catch/pet_form.html'

    def get(self, request):
        form = PetCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PetCreationForm(request.POST)
        if form.is_valid():
            new_pet = form.save(commit=False)
            new_pet.owner = request.user
            new_pet.image = 'dog.jpg'
            new_pet.save()
            data = form.cleaned_data
            form = PetCreationForm()
            return redirect('petPage')
        args = { 'form': form, 'text': data }
        return render(request, self.template_name, args)

class UserSignUpView(CreateView):
    model = PetUser
    fields = ('username', 'first_name', 'last_name','password','email','location','description')
    template_name = 'sign_up.html'
    success_url = reverse_lazy('homePage')

class UserEditProfileView(generic.UpdateView):
    model = PetUser
    fields = ('username', 'first_name', 'last_name','email','location','description',)# 'image')
    template_name = 'change_profile.html'
    success_url = reverse_lazy('profilePage')

    def get_object(self):
	    return get_object_or_404(PetUser, pk=self.request.user.id)

class UserViewProfileView(generic.ListView):
    model = PetUser
    fields = ('username', 'first_name', 'last_name','password','email','location','description', 'hosting', 'image')
    template_name = 'profilePage.html'
    def get_object(self):
        return get_object_or_404(PetUser, pk=self.request.user.id)

class UserViewPets(LoginRequiredMixin, generic.ListView):
    model = Pet
    template_name ='petPage.html'

    def get_queryset(self):
        return Pet.objects.filter(owner=self.request.user)

class UserViewEvents(LoginRequiredMixin, generic.ListView):
    model = Event
    template_name ='homePage.html'

    def get_queryset(self):
        return Event.objects.filter(host=self.request.user)

def events(request):
    events = Event.objects.all()
    context = {
        "events": events,
    }
    return render(request, 'eventsPage.html', context = context)

# def events(request):
#     events = Event.objects.all()
#     context = {
#         "events": events,
#     }
#     return render(request, 'eventsPage.html', context = context)

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

# def about(request):
#     model = PetUser
#     # pets = Pet.objects.filter(owner = model.username)
#     context = {
#         "owner" : PetUser,
#     }
#     return render(request, 'aboutPage.html', context = context)

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
