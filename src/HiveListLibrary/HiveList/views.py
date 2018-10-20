from django.shortcuts import render

from HiveList.models import Playlist, Contributor, Artist, Song, Genre, SongInstance, VoteInstance

# Create your views here.
def index(request):


    # Render the HTML tmeplate index.html with the data in the context variable
    return render(request, "index.html", context=context)
