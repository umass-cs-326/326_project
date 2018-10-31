import textwrap
import random
from datetime import datetime, timedelta, timezone
from django.db import models
from django.contrib.auth.models import User
from faker import Faker
from Catch.models import PetUser, Pet, Event
fake = Faker()


#Create PetUsers
PetUsers = []
for i in range(10):
    u_uname = fake.profile()['username']
    u_fname = fake.first_name()
    u_lname = fake.last_name()
    u_password = fake.password()
    u_email = fake.free_email()
    u_location = fake.address()
    u_description = fake.sentence(nb_words=20, variable_nb_words=True, ext_word_list=None)
    u_image = "user_images/" + str(i) + ".jpg"

    if i is 1:
        #this user is the one displayed on ProfilePage
        u_uname = "ProfileUser"

    petUser = PetUser(
        username = u_uname,
        first_name = u_fname,
        last_name = u_lname,
        password = u_password,
        email = u_email,
        location = u_location,
        description = u_description,
        image = u_image
    )

    petUser.save()
    PetUsers.append(petUser)

#Create Pets
Pets = []
for i in range(10):
    p_name = fake.first_name()
    p_pet_type = fake.word()
    p_breed = fake.word()
    p_description = fake.sentence(nb_words = 20, variable_nb_words = True, ext_word_list = None)
    p_owner = PetUsers[fake.random_int(0, len(PetUsers)) - 1]
    p_image = "pet_images/" + str(i) + ".jpg"

    pet = Pet(
        name = p_name,
        pet_type = p_pet_type,
        breed = p_breed,
        description = p_description,
        owner = p_owner,
        image = p_image
    )
    pet.save()
    Pets.append(pet)

#Create Events
Events = []
for i in range(10):
    e_name = fake.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None)
    e_host = PetUsers[fake.random_int(0, len(PetUsers)) - 1]
    e_location = fake.address()
    e_latitude = random.uniform(-180, 180)
    e_longitude = random.uniform(-180, 180)
    e_datetime = fake.date_time(tzinfo = timezone(timedelta(hours = -5)))
    e_capacity = random.randint(10,100)
    e_description = fake.sentence(nb_words=20, variable_nb_words=True, ext_word_list=None)
    e_image = "event_images/" + str(i) + ".jpg"
    e_duration = timedelta(hours = random.randint(1, 10))

    event = Event(
        name = e_name,
        host = e_host,
        location = e_location,
        latitude = e_latitude,
        longitude = e_longitude,
        datetime = e_datetime,
        capacity = e_capacity,
        description = e_description,
        image = e_image,
        duration = e_duration
    )
    event.save()
    event.pet.add(Pets[fake.random_int(0, len(Pets)) - 1])

    event.save()
    Events.append(event)

#book.genre.add(genres[fake.random_int(0, len(genres)) - 1])
for petUser in PetUsers:
    petUser.hosting.add(Events[0])


print("\nUser:")
for u in User.objects.all():
    print(u)
print()

print("\nPets:")
for p in Pet.objects.all():
    print(p)
print()

print("\nEvents:")
for e in Event.objects.all():
    print(e)
print()

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
