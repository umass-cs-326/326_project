import textwrap
from datetime import timedelta

# Create a super user to use the admin site.
from django.contrib.auth.models import User as adminUser
from faker import Faker

from catalog.models import Genre, Movie, Request, User, Match

fake = Faker()

# Create Genres
genres = [
    Genre(name="Science Fiction"),
    Genre(name="Satire"),
    Genre(name="Drama"),
    Genre(name="Adventure"),
    Genre(name="Romance"),
    Genre(name="Mystery"),
]

# Save the genres to the database
for genre in genres:
    genre.save()


# Create Movies
movies = []
for i in range(0, 10):
    m_title = fake.job()
    m_cast = fake.name()
    m_director = fake.name()
    m_summary = fake.sentence()
    m_duration = fake.random_int(120, 200)
    m_date = fake.past_date(start_date="-30d", tzinfo=None)
    movie = Movie(
        title=m_title, cast=m_cast, director=m_director, summary=m_summary, duration=m_duration, date=m_date
    )
    movie.save()
    movie.genre.add(genres[fake.random_int(0, len(genres)) - 1])
    movie.save()
    movies.append(movie)


# Create Users

users = []
for i in range(0, 10):
    u_fname = fake.first_name()
    u_lname = fake.last_name()
    u_username = u_fname + u_lname
    u_password = fake.itin()
    u_bio = fake.text(50)
    user = User(
        username=u_username, password=u_password, bio=u_bio
        )
    user.save()
    users.append(user)

print("Genre:")
for g in Genre.objects.all():
    print(g)


#    print(a)
#
print("\nUser:")
for b in User.objects.all():
    print(b)
#
# Retrieve a random book from model and print it.

# Get all movie:

print('------------------')
print('All movies:')
for movie in Movie.objects.all():
    print("\nExample Movie:")
    print(f"Title: {movie.title}")
    print(f"Cast: {movie.cast}")
    print(f"Director: {movie.director}")
    print(f"Summary:\n{movie.summary}")


username = "admin"
password = "admin"
email = "admin@326.edu"
adminuser = adminUser.objects.create_user(username, email, password)
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
