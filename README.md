# 326_project
326 Project - Team Knock_Out - Flick

To run:

download the latest copy of the repo

go to src/locallibrary, run init.sh then run python manage.py runserver 8080

submission 2 tag: project2_v1.1

To create a new user:

after running init.sh and python manage.py runserver 8080, go to localhost:8080/index/signup
Here you can sign up using a custom form, this would create a App user, as well as our Flick user profile

To Log in:

go to localhost:8080/index/login or click the Login button on the top nav bar
Here you can log in using the user you created, you would be redirect to your user profile page

To Log out:

go to localhost:8080/index/logout or click the Logout button on the top nav bar
Here you can log out from your user account

To Edit Profile (User interaction with forms):

Go to your user profile page, for example, you are logged in as user1 (assuming you have created an user named user1), go to localhost:8080/index/user/user1.
Here you will see a form that would allow you to input new information (bio/picture url/gender).  Once you click submit it would update the database, and the user page would reflect that change in real time.

Note: the form would not appear if you are not looking at the correct profile.  Also the user could only modify their own profile.
