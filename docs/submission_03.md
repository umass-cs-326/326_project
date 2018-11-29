# Project 3 - Team Writeup

Overview: A brief overview of your application. Please highlight any changes from your project proposal since the Project 2 submission.
Our team is creating an application where an individual can schedule a time, request a party of up to 5 people, and match with those people to watch a movie of their choice. It is called “Flick”. The whole idea of this application is so that no one has to watch a movie alone if they don’t want to, and can use this application to make friends around the UMass or Five College campuses. This application consists of 5 web pages, a homepage where all the movies are listed, a page where an individual can request to watch a specific movie at a certain time of their choice, and a location of their preference with people they want to watch it with. 
*The changes that occurred during this project were user authentication and interaction through forms involved with our web application that includes the login functionality and authentication.*

Team Members: A list of your team members:
- Apoorva Karpurapu 
- Kuhu Wadhwa
- Damin Zhang
- Long To
- Frick Shao
- Kurtis Chau

Video Link: A link to your YouTube video regarding this submission. See below: 

Design Overview: 
We as a team implemented the login functionality in our web application, and enabled the ability for authentication, authorization, and session support, as well as user interaction with database. We created the login page from Django itself from its token based authentication. Then, in the views classes we implemented can provide a direct instance given a request from the database.  For user interaction we implemented sign up with custom form, as well as profile editing.  User can create a new user profile, which would add a new profile containing the input bio/profile picture url/gender to our database.  Once they are logged in, user could edit their own profile, which would update/modify their user profile in the database.  


Problems/Successes: A brief overview of the problems and successes your team encountered. This includes team communication problems/successes, what worked and what didn’t, implementation problems/successes, what worked and what didn’t, and what your team can do to improve collaboration and implementation for the next Project submission.

Problems:

- Scheduling issues, some of the people in our group couldn’t meet up and had time conflicts.
- Some of our team members were running old versions of Django, so running the application was an issue at times.
Run into several errors through the process of authentication.
- Django default user doesn't create a internal user profile. 
- Difficulty creating custom signup form, and have it create a new User, as well as a new Profile

Successes:

- Through the collaboration, we were able to individually finish our portions of the project and completing it successfully based on the feedback.
- Fixed errors quickly, and allocated time for risks/improvements of the user interface.
- Modified our model so that User would align with Profile 
- Created Custom form for user interaction (create new profile with various input)
-  Implemented Profile Editing functionality with correct permission set up

Instruction (pasted from readme):
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

