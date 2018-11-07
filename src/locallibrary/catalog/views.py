from django.shortcuts import render
#the urls here will change based on the names we give the templates and where we put the templates
from catalog.models import Movie, User, Request, Match
from django.views import generic

##picture of movie; urls for movie and username and index; using function instead of class
##what does match need; what primary key of movie; hard for users to remember id
def index(request):
    return render(request, "index.html")

def movie(request):
	return render(request, "movie.html")

def user(request):
	return render(request, "user.html")

# class UserDetailView(generic.DetailView):
# 	model = User
# 	template_name = "user.html"

# class Movie(generic.ListView):
# 	model = Movie
# 	template_name = "movie.html"

# class MovieDetailView(generic.DetailView):
# 	model = Movie
# 	template_name = "movie_detail.html"	
		
