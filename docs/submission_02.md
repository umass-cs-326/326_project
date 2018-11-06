Overview<br>
	Classdoor is a very creative and unique spin off of the well-know job searching website “Glassdoor”. Classdoor gives users the ability to not only search for classes and be given recommended classes but also to socialize with fellow peers who may have taken the class in semesters prior. They can view average grades and difficulty of a particular course and get a sneak peek at the professor. Along with a university’s online class portal Classdoor is a one stop shop for all students needs when looking for a class. 
	Since Project 1 a lot of additions and functionality have been added to Classdoor. Some of the highlights though are are data models, URL routing, and HTML templates giving our app some dynamic abilities. We will dive into these later on but overall Classdoor has transformed from a bunch of separate web pages into an actual web app. 

Team Members<br>
	Nathan Blue,
	Spencer Rendano,
	Zander Bobronnikov,
	Zihang Zhou,
	Amine Kebichi,
	Matthew Dahl,

Video Link

[Insert link here]

Design Overview<br>
	Models - 
		The hardest part about making the models was actually determining what needed to be included. It was helpful to draw it out but it was still tough until we really started working with it to see what was needed. For our design we decided to pick 6 data models to work with to give us the right balance of fields per model (we tried to keep it between 3-10). We then had to decide the best option for how to represent each field, whether it should be a DecimalField, CharField, or if it should utilize one of our own models using a ForeignKey. This also included thinking about if a field would need to be one to one or many to many etc.. It was a lot of testing and working with the django admin site to get it the way that we needed for the project.<br>
	URL Routes - 
		We generated unique URLs for all of our pages. This is implemented using an array “urlpatterns” which consists of multiple path() functions. Within the path functions, the first parameter is a string (the url), the second parameter maps to the views function to render the webpage (we will speak more about this below) and the third parameter is a name. The empty string “” is mapped to the url for our home page. We initially ran into difficulty with the syntax for trying to generate pages for specific entries in the database. For example, on the write review page, we use the classifier “review/<int:id>” which passes the class id as a parameter to the associated view function. Because a page to write a review should be associated with a specific class, we also implemented paths to redirect users if they try to access an common url such as “/review/” without a class id appended to the end. <br>
	UI Views - 
		In Views.py we defined views to call render() which accepts a request object (Http information including path and body), an HTML template, and a context parameter. This is where we handle dynamic content, by defining a context and passing it to the render function. This ensures that when the specified html file is rendered, dynamic content (context) can be used in areas surrounded by double brackets {{ }}. For the class and feed pages, we had to parse specific content to from our models and pass this as context to properly display all data from our relational database. 

Problems/Successes<br>
	Problems - 
		So far our team has done an excellent job with working together. It is hard to pick out a lot of problems but a few that could use more work would be, being very clear with what each of us is working on to minimize the amount of duplicate work we are doing(although this does help everyone understand it a little better). Also, finding meeting times that work for all of us has been a problem. We have made it work but has definitely not been ideal.
		In terms of our project itself we have done a great job of figuring things out fairly quickly. We really had no major issues with any aspects of the project. I think figuring out how to get the templates working took a little time but eventually got it and now is working great!<br>
	Successes - 
		Our group has had incredibly good communication. Whether it be through slack or texting if we need a really quick response, everyone has stepped up in a big way when it comes to answering questions. Some in the group have more experience with these systems and have been more than helpful when others ask for it. We also did a much better job this project delegating work and getting things done earlier. 
		For the technical side of things we have done such a good job making our pages look presentable and allowing all of our backend side of things run smoothly. All in all we are all happy with the work we have done so far.
