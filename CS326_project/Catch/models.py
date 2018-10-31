from django.db import models
from django.urls import reverse
from datetime import timedelta

# Create your models here.
class PetUser(models.Model):
    username = models.CharField(max_length = 30)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 30)
    location = models.CharField(max_length = 100, blank = True, null = True, help_text = "Your area of residence")
    description = models.CharField(max_length = 3000, blank = True, null = True)
    image = models.ImageField(upload_to = "user_images", null = True)

    hosting =  models.ManyToManyField("Event")

    def __str__(self):
        return self.first_name + " " + self.last_name

class Pet(models.Model):
    name = models.CharField(max_length=30)
    pet_type = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(max_length=3000, blank=True, null=True)
    image = models.ImageField(upload_to = "pet_images", null = True)
    owner = models.ForeignKey(PetUser, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    host = models.ForeignKey(PetUser, on_delete=models.PROTECT)
    pet = models.ManyToManyField(Pet)
    location = models.CharField(max_length=30, blank=True, null=True,
        help_text="Please be as specific as possible. Include the building and room number if applicable. A kind reminder, it is best to meet in public places."
    )
    latitude = models.FloatField(null = True)
    longitude = models.FloatField(null = True)
    datetime = models.DateTimeField()
    capacity = models.IntegerField()
    description = models.TextField(null=True)
    image = models.ImageField(upload_to = "event_images", null = True)
    duration = models.DurationField(default = timedelta(minutes=60))

    def __str__(self):
        return self.name
