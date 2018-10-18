from django.db import models
from django.urls import reverse

class Class(models.Model) :
    """Model representing a UMass class"""

    name = models.CharField(max_length=100, help="Enter class name")
    code = models.CharField(max_length=15, help="Enter class code")

    def __str__(self) :
        return f"{self.code} {self.name}"

    

# Create your models here.
