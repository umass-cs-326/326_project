from classdoor.models import Subject, ClassDesc, University, Review
from faker import Faker
from django.contrib.auth.models import User
from datetime import timedelta
import textwrap

fake = Faker()

# grades = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]

# Create Subjects
subjects = [
    Subject(name="Computer Scence", abbreviation="CS"),
    Subject(name="Biology", abbreviation="BIO"),
    Subject(name="Mathematics", abbreviation="MATH"),
    Subject(name="English", abbreviation="ENG"),
]

# Save the subjects to the database
for subj in subjects:
    subj.save()

# Create Universities
unis = []

for i in range(1, 3):
    uName = "University of " + fake.city()
    uAddress = fake.address()

    uni = University(name=uName, location=uAddress)

    uni.save()

    for subj in subjects:
        uni.subjects.add(subj)

    uni.save()
    unis.append(uni)

# Create Classes
classes = []
for i in range(1, 10):
    subject = subjects[fake.random_int(0, len(subjects) - 1)]
    uni = unis[fake.random_int(0, len(unis) - 1)]

    cName = subject.abbreviation + str(fake.random_int(100, 500))
    cTeacher = fake.name()
    cDesc = fake.text(1000)
    cAvgGrade = fake.random_int(0, 100)
    cStarRating = float(fake.random_int(0, 500)) / 100.0

    c = ClassDesc(name=cName,
              teacher=cTeacher,
              description=cDesc,
              averageGrade=cAvgGrade,
              starRating=cStarRating,
              subject=subject,
              university=uni)

    c.save()

    uni.classes.add(c)
    uni.save()

    classes.append(c)


# Create Reviews
reviews = []
for i in range(0, len(classes) - 1):
    currClass = classes[i]
    rGrade = fake.random_int(0, 100)
    rStarRating = float(fake.random_int(0, 500)) / 100.0

    for j in range(1, fake.random_int(3, 20)):
        rTitle = fake.text(10)
        rText = fake.text(200)

        review = Review(title=rTitle,
                        text=rText,
                        gradeReceived=rGrade,
                        starRating=rStarRating,
                        classDesc=currClass)

        review.save()
        reviews.append(review)

        currClass.reviews.add(review)
        currClass.save()

print('Subjects:')
for s in Subject.objects.all():
    print(s)

print('\nUniversities:')
for u in University.objects.all():
    print(u)

print('\nClasses:')
for c in ClassDesc.objects.all():
    print(c)

print('\nReviews:')
for i in Review.objects.all():
    print(i)

username = "admin"
password = "admin"
email = "admin@admin.admin"
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

