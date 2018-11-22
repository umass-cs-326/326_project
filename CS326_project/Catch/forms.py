 from django import forms
 from .models import PetUser
# from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _

# class ChangeProfileForm(forms.Form):
#     email = forms.EmailField(max_length = 30, required=True)
#     #email = forms.EmailField(max_length = 30)
#     #description = forms.CharField(max_length = 3000, blank = True, null = True)

#     def clean_email(self):
#         data = self.cleaned_data['email']
        
#         # Check if length>=6 
#         # if data.is_valid == False :
#         #     raise ValidationError(_('Invalid email format, please try again.'))

#         # Remember to always return the cleaned data.
#         return data


class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length = 30)
    first_name = forms.CharField(max_length = 30)
    last_name = forms.CharField(max_length = 30)
    password = forms.CharField(max_length = 30)
    email = forms.EmailField(max_length = 30)
    location = forms.CharField(max_length = 100)
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = PetUser
        fields = ('username', 'first_name', 'last_name','password','email','location','description')