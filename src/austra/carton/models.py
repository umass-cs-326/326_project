from django.db import models
from django.urls import reverse

class Class(models.Model) :
    """Model representing a UMass class"""

    name = models.CharField(max_length=100, help="Enter class name")
    code = models.CharField(max_length=15, help="Enter class code")

    def __str__(self) :
        return f"{self.code} {self.name}"

class ClassInstance(models.Model) :
    """Model representing a UMass class instance"""
    Class = models.ForeignKey("Class", on_delete=models.SET_NULL, null=True)
    profs = models.CharField(max_length=100, help="Enter professor(s) name")

    def __str__(self) :
        return f"{self.Class} {self.profs}"
    

