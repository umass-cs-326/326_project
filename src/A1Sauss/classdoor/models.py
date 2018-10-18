from django.db import models

# Create your models here.

class ClassDesc(models.Model):
   """Model representing an library event."""

   name = models.CharField(max_length=200)
   #tags = models.models.ManyToManyField(Class, help_text="Select a preReq for this class")
   teacher = models.CharField(max_length=200)
   #reviews = models.ArrayField()
   description = models.CharField(max_length=200)
   rating = models.IntegerField()
   avgGrade = models.IntegerField(max_length=10)
   #preReqs = models.ManyToManyField(Class, help_text="Select a preReq for this class")
   #subject = models.ManyToManyField(Subject, help_text="Select a preReq for this class")
   #university = models.CharField(max_length=200)
   #genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")



   class Meta:
       ordering = ['name']

   def get_absolute_url(self):
       """Returns the url to access a particular author instance."""
       return reverse('event-detail', args=[str(self.id)])

   def __str__(self):
       """String for representing the Model object."""
       return f'{self.title}'