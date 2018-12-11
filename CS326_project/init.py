import textwrap
import random
from datetime import datetime, timedelta, timezone
from django.db import models
from django.contrib.auth import get_user_model
from faker import Faker
from Catch.models import PetUser, Pet, Event
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType

fake = Faker()


PetOwners, created = Group.objects.get_or_create(name ='PetOwners')

PetUser_content = ContentType.objects.get_for_model(PetUser)
Pet_content = ContentType.objects.get_for_model(Pet)
Event_content = ContentType.objects.get_for_model(Event)

PetUser_perms = Permission.objects.filter(content_type=PetUser_content)
Pet_perms  = Permission.objects.filter(content_type=Pet_content)
Event_perms = Permission.objects.filter(content_type=Event_content)

g = Group.objects.get(name='PetOwners')

for p in PetUser_perms:
    g.permissions.add(p)
for p in Pet_perms:
    g.permissions.add(p)
for p in Event_perms:
    g.permissions.add(p)


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

g = Group.objects.get(name='PetOwners')
for u in PetUsers:
    g.user_set.add(u)

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
    e_latitude = random.uniform(42.371915, 42.412205)
    e_longitude = random.uniform(-72.549531, -72.496386)
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
for u in get_user_model().objects.all():
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


# admins, created = Group.objects.get_or_create(name = "admin")
# perms = Permission.objects.all()
#
# a = Group.objects.get(name="admin")
# for p in perms:
#     a.permissions.add(p)
#
# admin = PetUser(
#     username = "compsci326",
#     first_name = "compsci326",
#     last_name = "compsci326",
#     password = "compsci326",
#     email = "admin@326.edu",
#     location = fake.address(),
#     description = fake.sentence(nb_words=20, variable_nb_words=True, ext_word_list=None),
#     image = "user_images/1.jpg"
# )
# admin.save()
# a.user_set.add(admin)
#
# admin.is_superuser = True
# admin.is_staff = True
# admin.save()

username = "compsci326"
password = "compsci326"
email = "admin@326.edu"
adminuser = get_user_model().objects.create_user(username, email, password)
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
