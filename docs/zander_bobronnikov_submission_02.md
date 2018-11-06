
I worked on many aspects of this project. The first of which was doing the initial init.py and init.sh setup. I worked on faking data for all of the models Matt and Zihang created. I also helped fix up a few things in the models.py file. In init.py I also created a super user in init.py.

I also worked on the template for my page, the feed of classes. This was more difficult than anticipated because I had a list of classes but I needed more than just the basic data for each class. For example, I had to separate each class name into 'subject' and 'number' (e.g. 'CS' and '326') and I had to generate a featured review based on the reviews for each class. To do this I generated an array of dictionaries python in my views.py function and passed this in the context. This allowed me to do the separation and querying for a review of that class in python. 

Next I worked on updating the navbar in the main template to, one connect to the other pages, and two, show which page is active. To show which page is active I used {% if %} tags to check the text of the url to see which page name it contained. I used the { % url % } tags to link to other pages and also changed the font of the title.

Finally I worked on part of the video that showed the feed page and how that connects to the data model by screen recording my code and the feed page with voiceover.

