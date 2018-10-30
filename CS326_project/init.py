import textwrap
from datetime import datetime
from datetime import timedelta
from PIL import Image as PImage #####################
from django.db import models #################
from django.core.files.uploadedfile import SimpleUploadedFile ###############
# Create a super user to use the admin site.
from django.contrib.auth.models import User
from faker import Faker

from Catch.models import Pet, PetUser, Event, Image
# Author, Book, BookInstance, Genre
fake = Faker()



# Create Images
Images = []
for i in range(0, 9):
    image_instance = Image()
    img = models.ImageField(default="dog_images/"+str(i)+".jpg")
    image_instance = Image(image="dog_images/"+str(i)+".jpg")
    image_instance.save()
    Images.append(image_instance)

print("\nImages:")
for u in Image.objects.all():
    print(u)

# Create Authors
PetUsers = []
for i in range(1, 10):
    u_uname = fake.word()
    # fake.first_name()
    u_fname = fake.first_name()
    u_password = fake.password()
    u_email = fake.free_email()
    u_location = fake.address()
    u_description = fake.sentence(nb_words=20, variable_nb_words=True, ext_word_list=None)
    petUser = PetUser(
        username = u_uname, first_name=u_fname, password = u_password, email = u_email, location = u_location, description = u_description,
    )
    petUser.save()
    PetUsers.append(petUser)

#Create Pets
Pets = []
for i in range(1, 10):
    p_name = fake.first_name()
    p_pet_type = fake.word()
    p_breed = fake.word()
    p_description = fake.sentence(nb_words=20, variable_nb_words=True, ext_word_list=None)
    p_owner = PetUsers[fake.random_int(0, len(PetUsers)) - 1]
    pet = Pet(name=p_name, pet_type=p_pet_type, breed=p_breed, description=p_description, owner = p_owner)
    pet.save()
    #pet.image.add(Images[fake.random_int(0,len(Images))-1])
    Pets.append(pet)

#Create Events
# class datetime.datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
x = datetime(1995, 12, 12)
Events = []
for i in range(1, 10):
    e_pet_owner = PetUsers[fake.random_int(0, len(PetUsers)) - 1]
    # e_pet = Pets[fake.random_int(0, len(Pets)) - 1]
    # e_pet = Pets[0:3]
    e_location = fake.address()
    e_datetime = x
    # e_datetime = fake.date_of_birth() + timedelta(days=365 * fake.random_int(65, 100))
    # e_capacity = fake.random_number(digits=None, fix_len=False)
    e_capacity = 5
    e_description = fake.sentence(nb_words=20, variable_nb_words=True, ext_word_list=None)
    # e_duration = fake.random_number(digits=None, fix_len=False)
    e_duration = timedelta(1, 2, 3)
    event = Event(pet_owner = e_pet_owner, location = e_location, datetime = e_datetime, capacity = e_capacity, description = e_description, duration = e_duration)
    event.save()
    event.pet.add(Pets[fake.random_int(0, len(Pets)) - 1])
    event.save()
    Events.append(event)

print("\nPetUser:")
for u in PetUser.objects.all():
    print(u)


print("\nPets:")
for u in Pet.objects.all():
    print(u)



username = "compsci326"
password = "compsci326"
email = "admin@326.edu"
adminuser = User.objects.create_user(username, email, password)
adminuser.save()
adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()
message = f"""
====================================================================
The database has been setup with the following credentials:

  username: {username}
  password: {password}
  email: {email}

You will need to use the username {username} and password {password}
to login to the administrative webapp in Django.

Please visit http://localhost:8080/admin to login to the admin app.
Run the django server with:

  $ python3 manage.py runserver 0.0.0.0:8080"
====================================================================
"""
print(message)
