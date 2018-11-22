from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import PetUser

class PetUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length = 30)
    first_name = forms.CharField(max_length = 30)
    last_name = forms.CharField(max_length = 30)
    password = forms.CharField(max_length = 30)
    email = forms.EmailField(max_length = 30)
    location = forms.CharField(max_length = 100)
    description = forms.CharField(widget=forms.Textarea)

    class Meta(UserCreationForm):
        model = PetUser
        fields = ('username', 'first_name', 'last_name','password','email','location','description')

class PetUserChangeForm(UserChangeForm):
    username = forms.CharField(max_length = 30)
    first_name = forms.CharField(max_length = 30)
    last_name = forms.CharField(max_length = 30)
    email = forms.EmailField(max_length = 30)
    location = forms.CharField(max_length = 100)
    description = forms.CharField(widget=forms.Textarea)

    class Meta(UserCreationForm):
        model = PetUser
        fields = ('username', 'first_name', 'last_name','email','location','description')