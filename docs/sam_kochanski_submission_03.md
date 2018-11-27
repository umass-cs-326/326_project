I contributed to Austra by implementing the user authentication/authorization system. This utilized django’s prefabricated permissions and user class. Originally I designed it to extend the abstract user class to apply custom permissions with user groups, but changed it when I realized most of this work was already done by django.

I designed and built the in-app forms for adding instructors and courses. I implemented them using default views from django. While this granted less flexibility, it simplified the system and let me use tableview in the templates.

Lastly, I implemented url-routing with django’s ?next keyword. This make it impossible for the wrong user to be on the wrong page, organized our view hierarchy, and fleshed out the user experience of the app.
