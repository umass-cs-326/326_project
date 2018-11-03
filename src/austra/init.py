# import textwrap
# from datetime import timedelta

# Create a super user to use the admin site.
from django.contrib.auth.models import User
from faker import Faker
import random

from carton.models import Class, Instructor, Session

fake = Faker()

# Create Classes
class_names = [
    # The compsci classes
    "121 Introduction to Problem Solving with Computers",
    # Either compsci 186 or 187
    "186 Using Data Structures",
    "187 Programming with Data Structures",

    "220 Programming Methodology",
    "230 Computer Systems Principles",
    "240 Reasoning About Uncertainty",
    "250 Introduction to Computation",
    "MATH 131 Calculus I",
    "MATH 132 Calculus II",
    # Either Math 233 or Statistic 515
    "MATH 233 Multivariate Calculus",
    "STATISTC 515 Statistics I",

    "MATH 235 Introduction to Linear Algebra",
    "311 Introduction to Algorithms",
]

# Construct the Class objects
# Extrapolate the class number from the class
# Set the starting rating to a random one between 1-5
classes = [
    # Keep in mind this is mock data for the ratings
    Class(name=name, code=next(word for word in name.split(" ") if word.isdigit()), rating=random.uniform(1, 5))
    for name in
    class_names
]

# Save the classes to the database
for c in classes:
    c.save()

# Create Instructors
mock_instructors = []
for _ in range(10):
    mock_name = (fake.first_name(), fake.last_name())
    mock_rating = random.uniform(1, 5)
    # Add the instructor the list
    mock_instructors.append(Instructor(name="{0}, {1}".format(*mock_name), rating=mock_rating))
    # Add the last created instructor
    mock_instructors[-1].save()

# Create the class Sessions
mock_sessions = []
for c in classes:
    # Add up to 3 sessions of the same class
    for _ in range(random.randint(1, 3)):
        mock_sessions.append(Session(cur_class=c, instructor=random.choice(mock_instructors)))
        mock_sessions[-1].save()

print("Classes:")
for c in Class.objects.all():
    print(c)

print("\nInstructors:")
for instructor in Instructor.objects.all():
    print(instructor)

print("\nSessions:")
for session in Session.objects.all():
    print(session)

# Retrieve a random session from our model and print it.
num_sessions = Session.objects.count()
random_session = random.choice(Session.objects.all())

print("\nExample Session:")
print(f"Session class name: {random_session.cur_class.name}")
print(f"Session instructor: {random_session.instructor.name}")
print(f"Session rating: {random_session.rating}")
print(f"Session class rating: {random_session.cur_class.rating}")
print(f"Session instructor rating: {random_session.instructor.rating}")


username = "admin"
password = "admin"
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
