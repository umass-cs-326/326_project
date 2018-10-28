import textwrap
from datetime import datetime
from datetime import timedelta

# Create a super user to use the admin site.
from django.contrib.auth.models import User
from faker import Faker

from Catch.models import Pet, PetUser, Event
fake = Faker()


# Create Authors
PetUsers = []
for i in range(1, 9):
    u_uname = fake.profile()["username"]
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

#One user to display in profiles
u_uname = "ProfileUser"
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
    Pets.append(pet)

#Create Events
Events = []
for i in range(1, 10):
    e_name = fake.sentence(nb_words=3, variable_nb_words=True, ext_word_list=None)
    e_pet_owner = PetUsers[fake.random_int(0, len(PetUsers)) - 1]
    e_location = fake.address()
    e_datetime = datetime(1995, 12, 12)
    e_capacity = 5
    e_description = fake.sentence(nb_words=20, variable_nb_words=True, ext_word_list=None)
    e_duration = timedelta(1, 2, 3)
    event = Event(name = e_name, pet_owner = e_pet_owner, location = e_location, datetime = e_datetime, capacity = e_capacity, description = e_description, duration = e_duration)
    event.save()
    event.pet.add(Pets[fake.random_int(0, len(Pets)) - 1])
    event.save()
    Events.append(event)

print("\nPetUser:")
for u in PetUser.objects.all():
    print(u)


print("\nPets:")
for p in Pet.objects.all():
    print(p)

# print("\nEvents:")
# for e in Events.objects.all():
#     print(e)

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
