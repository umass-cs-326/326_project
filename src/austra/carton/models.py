from django.db import models
from django.urls import reverse

class Class(models.Model) :
    """Model representing a UMass class"""

    name = models.CharField(max_length=100, help_text="Enter class name")
    code = models.CharField(max_length=15, help_text="Enter alphanumeric class code")
    rating = models.IntegerField()
    prereqs = models.ManyToManyField("self", null=True)
    def __str__(self) :
        return f"{code} {name}"

class Session(models.Model) :
    """Model representing a session"""
    cur_class = models.ForeignKey("Class", on_delete=models.CASCADE, null=True)
    instructor = models.ForeignKey("Instructor", on_delete=models.SET_NULL, null=True)
    max_seats = models.IntegerField()
    rating = (self.cur_class.rating + self.instructor.rating) if instructor is not None else None
    
    
    #TODO: verify this is proper usage of reverse(). Where is self.id declared?
    def get_absolute_url(self) :
        return reverse("session-detail", args=[str(self.id)])

class Instructor(models.Model) :
    """Model representing an instructor"""
    name = models.CharField(max_length=50, help="Enter instructor name")
    rating = models.IntegerField()

    def __str__(self) :
        return f"{self.name}"

    def get_absolute_url(self) :
        return reverse("instructor-detail", args=[str(self.id)])
