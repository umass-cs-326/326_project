from django.db import models
from django.urls import reverse
import datetime
from django.contrib.auth.models import User

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

def get_future(start_time=None, n_hours=1):
    """A function that returns a datetime object n_hours from now, or a passed datetime object"""
    if start_time is None:
        start_time = datetime.datetime.now()
    return start_time + datetime.timedelta(hours=n_hours)

class Session(models.Model) :
    """Model representing a session"""
    course = models.ForeignKey("Course", on_delete=models.CASCADE, null=True)
    instructor = models.ForeignKey("Instructor", on_delete=models.SET_NULL, null=True)
    max_seats = models.IntegerField()
    start_time = models.DateTimeField(default=datetime.datetime.now, help_text="Enter when the class starts", null=False)
    end_time = models.DateTimeField(default=get_future, help_text="Enter when the class ends", null=False)
    # days of the week
    # represent as a string to day thing mtwrf
    dow = models.CharField('', max_length=5, help_text="Enter days of the week", null=True)



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

#class DootRecord(models.Model):
#    is_updoot = models.BooleanField
#    course = models.ForeignKey("Course", on_delete=models.CASCADE, null=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #This is basically a list of classes that the user is looking to take
    sessions_current = models.ManyToManyField(Session)
    #This is basically a list of classes that the user has taken in the past
    courses_past = models.ManyToManyField(Course)
    #This will be a list of courses that this user has updooted or downdooted
    #courses_dooted = models.ManyToManyField(Course)
