from django.contrib import admin
from .models import PetUser, Pet, Event

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import PetUserCreationForm, PetUserChangeForm
from .models import PetUser


# Register your models here.
# admin.site.register(PetUser)
admin.site.register(Pet)
admin.site.register(Event)


class PetUserAdmin(UserAdmin):
    add_form = PetUserCreationForm
    form = PetUserChangeForm
    model = PetUser
    list_display = ['email', 'username', 'image']

admin.site.register(PetUser, PetUserAdmin)
