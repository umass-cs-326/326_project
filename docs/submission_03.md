# themeatbirds' Austra

# Overview
Austra is designed to fulfill a main goal of SPIRE, for students to determine which classes they will be taking and fill out their schedule, in a more intuitive way. Austra’s primary advantage is easily visualization how course candidates conflict and mesh with the graphical interface. Furthermore, it allows for student-oriented feedback for classes and teachers in one place. Austra has social features including profiles and comments. 

**What Changed**
We fleshed out the application. Users authentication was fully implemented, and extended into user profiles. Class tracking was associated with profiles, so that users can add classes directly to and from their profile. Admin users have special privileges, and they can now add instructors, courses and sessions directly to the database through the web application without needing the admin site. Searching for classes on the main calendar page and dooting (rating) classes was implemented.
# Team Members
* CJ Moynihan		partyrico
* Harrison Orne		vgaparadise
* Arielle Rosenthal	ariellerosen
* Sam Kochanski	bakerdonkey
# Video Link
https://youtu.be/XUPpYh_OZ6Y 
# Design Overview
**Authorization/Authentication**

There are two user groups - standard users and admins. Standard users can modify their schedule by selecting existing course sessions, while admins can create courses, instructors, and sessions in-app. Admins can delete instructors and classes, while users can only remove classes from their schedule. 

**Profile**

User profiles were hooked up with real data structures in an object called Profile. Here, there are two fields, one for courses_past and courses_current, which refer to courses the user has taken and courses they want to take respectively. The Profile adds to courses_past and the calendar adds to courses_current. 

**Calendar Design**

Adding and removing classes from the calendar was simple. We just checked for “added” or “removed” in the POST request, and did the action right inside of the view. 

**Comments**

Implementing comments would have been straight forward if it weren’t for the technical difficulties of django generic views and forms. We ended up overriding the post method twice, and doing the actual database work inside of a class that inherited from SingleObjectMixin. 

**Dooting**

Each user has a list of updooted and downdooted courses. These lists are incremented when the user presses the updoot or downdoot button, which submit post requests associating the respected buttons. The buttons are hidden if the user has already dooted. 

**Searching**

A search method was created and abstracted so that courses can be searched using the search function in models.py. It breaks apart a search into each word, then applies that search on the course names, the instructors, and the class codes. Results are sorted by class code, then by frequency of return, so that if a class matches multiple search terms it will float to the top, while classes that match only one term will be at the bottom.
This was implemented in the calendar accordion as a way to choose which classes to add and remove from the calendar, as well as the profile page to add and remove classes from past courses taken.
# Problems/Successes

**Problems:**
Authentication was overengineered -- we did not have to create custom permissions that serve the same purpose as the default CRUD permissions (for each model) created by django. Therefore, we simplified our system and it proved more stable and consistent. 

Implementing updooting, downdooting, and commenting proved to be difficult because we were trying to jam forms into a premade, generic DetailView. Django seemed to be severely limited in this case, and that hindered development. 


**Successes:**
**Search**
The search function works well. It checks across class code, instructor name and course name. For each search term, each of these categories are searched (with a match in any or all counting as 1 hit), then the results are ordered by number of hits. With the abstraction that has been implemented, it would also be quite feasible to extend the search to include more features to search on, or to include special attributes like quotes or AND, OR and NOT as special keywords.

**Profile**
In order to store the data tied to each user, something had to be done. The traditional user model is not implemented in models.py, but rather something that Django handles naively. Due to the special nature of the user model, it isn’t something that can be easily extended and modified. Rather than create an AbstractUser model, we determined it would be better to instead create a new model, Profile, that has a one-to-one relationship with the users. This is convenient because whenever the data that is used in profile is encapsulated and easy to modify or add to in the future.
There was some difficulty initially with creating the profiles and users all the time, so instead we used signals so that whenever a user is created, a post_save signal creates and pairs a profile. This way, users always have a fresh profile attached to them.

Despite many struggles dealing with Django, we didn’t give up and eventually made every form work to its full capacity. We had to try several different approaches for comments and dooting in particular. 

# Team Choice
The existing search is already something beyond the scope of what we’ve talked about in class, but there is room for improvement. Our team choice is extending our existing search implementation with powerful functions such as category-specific queries as well as quantifier searches such as >300. 

