from classdoor.models import Subject, Class, University, Review
from faker import Faker
from datetime import timedelta
import textwrap

fake = Faker()

grades = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]

# Create Subjects
subjects = [
    Subject(name="Computer Scence", abbrev="CS"),
    Subject(name="Biology", abbrev="BIO"),
    Subject(name="Mathematics", abbrev="MATH"),
    Subject(name="English", abbrev="ENG"),
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
    uni = subjects[fake.random_int(0, len(unis) - 1)]

    cName = subject.abbreviation + fake.random_int(100, 500)
    cTeacher = fake.name()
    cDesc = fake.text(1000)
    cAvgGrade = grades[fake.random_int(0, len(grades) - 1)]
    cStarRating = fake.random_int(0, 10)

    c = Class(name=cName,
              teacher=cTeacher,
              description=cDesc,
              average_grade=cAvgGrade,
              star_rating=cStarRating,
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
    rGrade = grades[fake.random_int(0, len(grades) - 1)]
    rStarRating = fake.random_int(0, 10)

    for j in range(1, fake.random_int(3, 20)):
        rTitle = fake.text(10)
        rText = fake.text(200)

        review = Review(title=rTitle,
                        text=rText,
                        grade=rGrade,
                        star_rating=rStarRating,
                        for_class=currClass)

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
for c in Class.objects.all():
    print(c)

print('\nReviews:')
for i in Review.objects.all():
    print(i)

# Retrieve a random book from model and print it.
books_count = Book.objects.count()
book = Book.objects.all()[fake.random_int(0, books_count - 1)]

print('\nExample Book:')
print(f'Title: {book.title}')
print(f'Author: {book.author}')
print(f'ISBN: {book.isbn}')
print(f'Summary:\n{textwrap.fill(book.summary, 77)}')

username = "compsci326"
password = "compsci326"
email = "compsci@326.edu"
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

