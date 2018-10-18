from django.db import models

# Create your models here.
class Events(models.Model):
    event_name = models.CharField(max_length=40)
    event_description = models.CharField(max_length=400)
    event_capacity = models.IntegerField()

class Pet(models.Model):
    pet_name = models.CharField(max_length = 40)
    pet_age = models.CharField(max_length=40)
    pet_description = models.CharField(max_length=400)
    pet_breed = models.CharField(max_length=40)
