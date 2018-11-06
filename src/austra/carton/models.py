from django.db import models
from django.urls import reverse

class Course(models.Model) :
    """Model representing a UMass class"""

    name = models.CharField(max_length=100, help_text="Enter class name")
    code = models.CharField(max_length=15, help_text="Enter alphanumeric class code")
    rating = models.IntegerField()
    prereqs = models.ManyToManyField("self", blank=True)
    def __str__(self) :
        return f"{self.code} {self.name}"

    def display_prereqs(self) :
        return ", ".join(prereqs.code for prereqs in self.prereqs.all())

class Session(models.Model) :
    """Model representing a session"""
    course = models.ForeignKey("Course", on_delete=models.CASCADE, null=True)
    instructor = models.ForeignKey("Instructor", on_delete=models.SET_NULL, null=True)
    max_seats = models.IntegerField()
    # TODO:
    # Start/End TIMES
    # MTWRF

    @property
    def get_rating(self) :
        #TODO check if null! This will fail if course or instructor is null
        return self.course.rating + self.instructor.rating

    #TODO: verify this is proper usage of reverse(). Where is self.id declared?
    def get_absolute_url(self) :
        return reverse("session-detail", args=[str(self.id)])

    def __str__(self) :
        return f"{self.course} with {self.instructor}"

class Instructor(models.Model) :
    """Model representing an instructor"""
    name = models.CharField(max_length=50, help_text="Enter instructor name")
    rating = models.IntegerField()

    def __str__(self) :
        return f"{self.name}"

    def get_absolute_url(self) :
        return reverse("instructor-detail", args=[str(self.id)])

class Comment(models.Model) :
    course = models.ForeignKey("Course", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50)
    comment_text = models.CharField(max_length = 500)
    date = models.DateTimeField(auto_now_add=True) #we set the date when we add it to the DB
