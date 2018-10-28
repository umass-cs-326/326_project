from django.contrib import admin
from .models import Image, PetUser, Pet, Event

# Register your models here.

admin.site.register(Image)
admin.site.register(PetUser)
admin.site.register(Pet)
admin.site.register(Event)
