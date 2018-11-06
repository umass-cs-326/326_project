# themeatbirds

# Austra

# Overview
Austra is designed to fulfill the main goal of SPIRE, for students to determine which classes they will be taking and fill out their schedule, in a more intuitive way. Austra’s main features include easily visualizing how classes conflict or mesh using the graphical interface, and viewing feedback for classes and teachers all in the same place. It has a variety of social features including profiles and comments. Just a few more and it would basically be Facebook!
## What Changed
* Tree.html put on the back burner because it would require the entry of relationships between classes and that is outside the scope of what our tool hopes to accomplish at this time
* Comments were implemented using an in-house model

# Team Members

* CJ Moynihan, partyrico
* Harrison Orne, vgaparadise
* Arielle Rosenthal, ariellerosen
* Sam Kochanski, bakerdonkey

# Video Link

# Design Overview
## Models
We were able to preserve most aspects of our original set of data models, while extending their features and attributes. Austra currently has three interconnected data structures -- instructors, courses, and sessions. Instructors have a name field and a rating field assigned by users. Courses have a name, a code for quick reference (eg. COMPSCI 220), and a rating determined by users. Furthermore, course has a many-to-many relationship with itself to define a list of prerequisites. Sessions are instances of course, and as such they reference a course and an instructor. Also, they have local start and end time, days of the week they are active, and a rating based on that of the instructor and course. Comments were added to our model directly instead of an external framework because we wanted more control of them. It has a one-to-many relationship with courses not sessions because only courses can have comments. 
## Views & Templates
Everything except the main.html (calendar) was straightforward and easy to implement. For a long time, the calendar didn’t display correctly, and when we integrated it with the base.html, it got even more broken. The cure turned out to be hosting the files directly, and this started a static files push where we used the built in Django static provisions. We have templates for both instructors and classes. Class lists are encoded in the sidebar of main.html and the teacher list has its own page. Both of these were implemented with generic Django views. In many places in the app, we exploited the fact that children models have a pointer to parent models and used the .all() method to find all instances of the child with the parent as a member. For example, on the class detail page, we used this construct to display the sessions (classes have a 1 to many relationship with sessions) for each class. 

We passed the model data into the templates using two major ways. As examples previously, the first was by creating view classes that inherit generic, which pass data by default when template is called. We used this to pass data like Course and Instructor data that needs to be able to access its references. The Session data (that is, individual sections of courses) is passed in directly when calendar is called in views.py. When views.py calls calendar, session and course data is tabulated into a list of lists that is passed directly as variables through the Django’s render shortcut. Then, the list of lists can be iterated using a for loop and Django’s list.list_num syntax.

## URLs
All of the important url routes are hooked up. Instructors and courses have their own pk routes, similar to the book example in the locallibrary. This enabled us to do fancy things in main.html such as link to specific classes as they are listed. 

# Problems/Successes
One of the issues we ran into was that making changes to models.py required rebuilding the `migrations/*` folder using:
`python3 manage.py makemigrations --merge`
The main issue with this method is that it caused file bloat over time. Whenever the merge is called, instead of deleting and modifying the previous files, Django would create additional wireframe files that would ‘merge’ the previous database structure with the new one. Eventually, we had to take a step back and figure out how to flush the migrations folder and rebuild it after we were finished making changes to models.py.

There was a lot of ambiguity when first defining and populating the course model since it needed a many-to-many relationship with itself. Since this was written before the project could be properly run, debugging the extremely sensitive syntax was difficult. Also, it was hard to tell if the entire operation was illegal to begin with, since populating the field took specific steps.

We’ve had some issues with git that were unexpected, but for the most part, the branch and merge technique worked really well. Everyone knew what they were working on, and were able to make their changes in their own branches before making a pull request. One major problem was when we made a single bad commit to the repo that deleted files. 30 minutes of Google searching and attempting to revert it finally succeeded when we set the HEAD of the remote two back. From then on, everyone was more careful about commiting directly to master and merging their own branches.

Trello was a great tool for us and a success. We used a Scrum methodology by clearly defining all of our tasks, then having each team member pull upcoming tasks into their working space, and then finally into the finished space. Overall, Trello was good because it enabled everyone to be productive and make progress on the project without stepping on each others’ toes.
