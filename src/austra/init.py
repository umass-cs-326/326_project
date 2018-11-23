# import textwrap
# from datetime import timedelta

# Create a super user to use the admin site.
from django.contrib.auth.models import User
from faker import Faker
import random
import datetime

from carton.models import Course, Instructor, Session, Comment


fake = Faker()

# Create Classes
class_names = [
    # The compsci classes
    "COMPSCI121 Introduction to Problem Solving with Computers",
    # Either compsci 186 or 187
    "COMPSCI186 Using Data Structures",
    "COMPSCI187 Programming with Data Structures",

    "COMPSCI220 Programming Methodology",
    "COMPSCI230 Computer Systems Principles",
    "COMPSCI240 Reasoning About Uncertainty",
    "COMPSCI250 Introduction to Computation",
    "MATH131 Calculus I",
    "MATH132 Calculus II",
    # Either Math 233 or Statistic 515
    "MATH233 Multivariate Calculus",
    "STAT515 Statistics I",

    "MATH235 Introduction to Linear Algebra",
    "COMPSCI311 Introduction to Algorithms",
]

# Construct the Class objects
# Extrapolate the class number from the class
# Set the starting rating to a random one between 1-5

# classes = [
#     # Keep in mind this is mock data for the ratings
#     Course(name=name, code=next(word for word in name.split(" ") if word.isdigit()).strip(), rating=random.randint(1, 5))
#     for name in
#     class_names
# ]
# classes = [
#     # Keep in mind this is mock data for the ratings
#     # dummy courses:
#     Course(name="Introduction to Problem Solving", code="COMPSCI121", rating=4),
#     Course(name="Programming with Data Structures", code="COMPSCI187", rating=3),
#     Course(name="Programming Methodology", code="COMPSCI220", rating=2),
#     Course(name="Reasoning About Uncertainty", code="COMPSCI240", rating=5)
#
# #    Course(name=name, code=next(word for word in name.split(" ")), rating=random.uniform(1, 5)) for name in class_names
#     ]
classes=list()
for course in class_names:
    code, _, name = course.partition(' ')
    rating = random.randint(1, 5)
    classes.append(Course(name=name, code=code, rating=rating))
    classes[-1].save()

max_prereqs = 2
for (index, course) in enumerate(classes):
    # Adds between 0 and max_prereqs, up to index, different random classes as prereqs
    for prereq_index in random.sample(range(index), random.randint(0, min(index, max_prereqs))):
        course.prereqs.add(classes[prereq_index])
    course.save()

# Create Instructors
mock_instructors = []
for _ in range(10):
    mock_name = (fake.first_name(), fake.last_name())
    mock_rating = random.uniform(1, 5)
    # Add the instructor the list
    mock_instructors.append(Instructor(name="{0} {1}".format(*mock_name), rating=mock_rating))
    # Add the last created instructor
    mock_instructors[-1].save()

#create mock comments
mock_comments = []
for c in classes :
    #add 1 to 10 comments
    for _ in range(random.randint(1, 6)):
        mock_comments.append(Comment(course=c, name=fake.name(), comment_text=fake.text(),date=fake.date_time))
        mock_comments[-1].save()
# Create the class Sessions
mock_sessions = []
print("pree session test")
for c in classes:
    # Add up to 3 sessions of the same class
    for _ in range(random.randint(1, 3)):
        # Choose a random hour for an arbitrary date
        start_time = datetime.datetime.combine(datetime.date(1, 1, 1), datetime.time(random.randint(8, 20)))
        mock_sessions.append(Session(
            course=c, instructor=random.choice(mock_instructors), max_seats=fake.random_int(10, 50),
            start_time=start_time, end_time=start_time+datetime.timedelta(hours=1),
            dow=random.choice(['mwf','tr'])
        ))
        print("Built but not saved mock_session")
        mock_sessions[-1].save()
        print("Saved mock_session")
print('post session test')

print("Classes:")
for c in Course.objects.all():
    print(c)

print("\nInstructors:")
for instructor in Instructor.objects.all():
    print(instructor)

print("\nSessions:")
for session in Session.objects.all():
    print(session)
print("Comments:")
for c in Comment.objects.all():
    print(c)

# Retrieve a random session from our model and print it.
num_sessions = Session.objects.count()
random_session = random.choice(Session.objects.all())

print("\nExample Session:")
print(f"Session class name: {random_session.course}")
print(f"Session class prereqs: {random_session.course.display_prereqs()}")
print(f"Session instructor: {random_session.instructor.name}")
print(f"Session rating: {random_session.get_rating}")
print(f"Session class rating: {random_session.course.rating}")

print(f"Session instructor rating: {random_session.instructor.rating}")


username = "admin"
password = "admin"
email = "admin@326.edu"
adminuser = User.objects.create_user(username, email, password)
adminuser.save()
adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()
user2 = User.objects.create_user('user', 'user@user.com', 'user')
user2.save()
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
