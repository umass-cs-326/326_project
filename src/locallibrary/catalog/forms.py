from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from catalog.models import Profile


class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    bio = forms.CharField(max_length=300,help_text='Describe yourself!')
    picture_url = forms.CharField(max_length=300,required=False,help_text='Optional.  Profile Pic')
    gender = forms.CharField(max_length=300,help_text='Gender')
    class Meta:
        model = User   #'first_name', 'last_name'
        fields = ('username', 'bio','picture_url','gender', 'password1', 'password2', )

class EditProfileForm(forms.Form):
    
    bio = forms.CharField(max_length=300)
    picture_url = forms.CharField(max_length=300,required=False)
    gender = forms.CharField(max_length=300)
    class Meta:
        model = Profile
        fields = ('bio','picture_url','gender')

