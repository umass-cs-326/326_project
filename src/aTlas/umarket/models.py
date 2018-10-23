from django.db import models

# Create your models here.
class User(models.Model):
	email = models.EmailField(max_length=254, help_text="Enter email address")
	password = models.CharField(max_length=40,help_text="Enter password")
	name = models.CharField(max_length=20, help_text="Full name")
	rating = models.IntegerField()
	profile_picture = models.ImageField(upload_to="where are we putting these", height_field=100, width_field=100, max_length=100)
	#userID = models.UUIDField()
	def __str__(self):
		return self.name
#class UserProfile(models.Model):
#	email = models.EmailField(max_length=254, help_text="Enter email address")
#	name = models.CharField(max_length=20, help_text="Full name")
#	rating = models.IntegerField()
#	profile_picture = models.ImageField(upload_to="where are we putting these", height_field=100, width_field=100, max_length=100)

class Product(models.Model):
	#productID = models.UUIDFIeld()
	#userID = same as userID from User class
	name=models.CharField(max_length=100, help_text="Product")
	description = models.TextField()
	price = models.DecimalField(max_digits=4, decimal_places=2)
	picture = models.ImageField(upload_to="where are we putting these", height_field=100, width_field=100, max_length=100)
	
	def __str__(self):
		return self.name
#class MeetUpLocation(models.Model):
#	location = models.CharField(max_length=100, help_text="Location meetup")
#class Category(models.Model):
#	name = models.CharField(max_length=100, help_text="Product category")
	

