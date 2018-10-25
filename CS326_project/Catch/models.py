from django.db import models
from django.urls import reverse

# Create your models here.

class Image(models.Model):
    image = models.ImageField()
    def __str__(self):
        return str(self.image)

class PetUser(models.Model):
    username = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    location = models.FloatField(max_length=30)
    description = models.CharField(max_length=3000)

    def __str__(self):
        return "Username: "+self.username 

class Pet(models.Model):
    name = models.CharField(max_length=30)
    pet_type = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    description = models.TextField(max_length=3000)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    owner = models.ForeignKey(PetUser, on_delete=models.PROTECT)

    def __str__(self):
        return "Pet name: "+self.name+" Owner: "+self.owner.username


class Event(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.PROTECT)
    pet_owner = models.ForeignKey(PetUser, on_delete=models.PROTECT)
    location = models.CharField(max_length=30)
    datetime = models.DateTimeField()
    capacity = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return "Location: "+self.location +" Date/Time"+str(self.datetime)



    

