from django.db import models

# Create your models here.

class ClassDesc(models.Model):
   """Model representing an library event."""

   name = models.CharField(max_length=200)
   #tags = models.models.ManyToManyField(Class, help_text="Select a preReq for this class")
   teacher = models.CharField(max_length=200)
   reviews = models.ManyToManyField('Review', help_text="Reviews for this class")
   description = models.CharField(max_length=200)
   rating = models.DecimalField(default=0.0, max_digits=4, decimal_places=2)
   avgGrade = models.DecimalField(default=0.0, max_digits=4, decimal_places=2)
   preReqs = models.ManyToManyField('self', help_text="Select a preReq for this class", blank=True)
   subject = models.ForeignKey('Subject', help_text="Select a subject for this class",  on_delete=models.SET_NULL, null=True)
   universityName = models.ForeignKey('University', max_length=200,  on_delete=models.SET_NULL, null=True)



   class Meta:
       ordering = ['name']

   def get_absolute_url(self):
       """Returns the url to access a particular author instance."""
       return reverse('event-detail', args=[str(self.id)])

   def __str__(self):
       """String for representing the Model object."""
       return f'{self.name}'


class Review(models.Model):
   """Model representing an library event."""

   title = models.CharField(max_length=200)
   text = models.CharField(max_length=500)
   starRating = models.DecimalField(max_digits=3, decimal_places=2)
   gradeReceived = models.DecimalField(max_digits=3, decimal_places=2)
   #tags = models.IntegerField(default=1)
   classDesc = models.ForeignKey('ClassDesc', help_text="Select a class for this description",  on_delete=models.SET_NULL, null=True)
   author = models.ForeignKey('User', help_text="Select a user for this review",  on_delete=models.SET_NULL, null=True)
   likes = models.IntegerField(default=0)
   dislikes = models.IntegerField(default=0)



   class Meta:
       ordering = ['title']

   def get_absolute_url(self):
       """Returns the url to access a particular author instance."""
       return reverse('event-detail', args=[str(self.id)])

   def __str__(self):
       """String for representing the Model object."""
       return f'{self.title}'


class University(models.Model):
   """Model representing an library event."""

   name = models.CharField(max_length=200)
   location = models.CharField(max_length=500)
   classes = models.ManyToManyField('ClassDesc')
   subjectsOffered = models.ManyToManyField('Subject', blank=True)
   

   class Meta:
       ordering = ['name']

   def get_absolute_url(self):
       """Returns the url to access a particular author instance."""
       return reverse('event-detail', args=[str(self.id)])

   def __str__(self):
       """String for representing the Model object."""
       return f'{self.name}'


class User(models.Model):
   """Model representing an library event."""

   username = models.CharField(max_length=15)
   email = models.CharField(max_length=30)
   password = models.CharField(max_length=20)
   major = models.ManyToManyField('Subject')
   writtenReviews = models.ManyToManyField('Review', blank=True)
   

   class Meta:
       ordering = ['username']

   def get_absolute_url(self):
       """Returns the url to access a particular author instance."""
       return reverse('event-detail', args=[str(self.id)])

   def __str__(self):
       """String for representing the Model object."""
       return f'{self.username}'

class Subject(models.Model):
   """Model representing an library event."""

   name = models.CharField(max_length=40)
   universityName = models.ForeignKey('University',  on_delete=models.SET_NULL, null=True, related_name='+')
   

   class Meta:
       ordering = ['name']

   def get_absolute_url(self):
       """Returns the url to access a particular author instance."""
       return reverse('event-detail', args=[str(self.id)])

   def __str__(self):
       """String for representing the Model object."""
       return f'{self.name}'




