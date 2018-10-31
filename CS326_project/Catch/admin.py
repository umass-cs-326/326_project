from django.contrib import admin
from .models import PetUser, Pet, Event

# Register your models here.
admin.site.register(PetUser)
admin.site.register(Pet)
admin.site.register(Event)
