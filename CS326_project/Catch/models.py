from django.db import models
from django.urls import reverse
from datetime import timedelta

# Create your models here.

class Image(models.Model):
    image = models.ImageField()
    def __str__(self):
        return str(self.image)

class PetUser(models.Model):
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    location = models.CharField(max_length=100, blank=True, null=True,
                                help_text="Your area of residence")
    description = models.CharField(max_length=3000, blank=True, null=True)

    def __str__(self):
        return self.username

class Pet(models.Model):
    name = models.CharField(max_length=30)
    pet_type = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(max_length=3000, blank=True, null=True)
    image = models.ManyToManyField(Image)
    owner = models.ForeignKey(PetUser, on_delete=models.PROTECT)

    def __str__(self):
        return "Pet name: "+self.name+" Owner: "+self.owner.username


class Event(models.Model):
    pet_owner = models.ForeignKey(PetUser, on_delete=models.PROTECT)
    pet = models.ManyToManyField(Pet)
    location = models.CharField(max_length=30, blank=True, null=True,
            help_text="Please be as specific as possible. Include the building and room number if applicable. A kind reminder, it is best to meet in public places.")
    datetime = models.DateTimeField()
    capacity = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ManyToManyField(Image)
    duration = models.DurationField(default = timedelta(minutes=60)) #format is now hr:min:sec -- write a method to reformat?

    def __str__(self):
        return "Location: "+str(self.location) +" Date/Time"+str(self.datetime)


#get absolute url??
