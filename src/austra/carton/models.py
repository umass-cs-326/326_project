from django.db import models
from django.urls import reverse

class Class(models.Model) :
    """Model representing a UMass class"""

    name = models.CharField(max_length=100, help="Enter class name")
    code = models.CharField(max_length=15, help="Enter class code")

    def __str__(self) :
        return f"{self.code} {self.name}"

class Session(models.Model) :
    """Model representing a session"""
    cur_class = models.ForeignKey("Class", on_delete=models.SET_NULL, null=True)
    instructor = models.ForeignKey("Instructor", on_delete=models.)

class Instructor(models.Model) :
    """Model representing an instructor"""
    name = models.CharField(max_length=50, help="Enter instructor name")
    def __str__(self) :
        return f"{self.name}"
