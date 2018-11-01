from django.shortcuts import render

from HiveList.models import Genre #Playlist, Contributors, Artist, Song, Genre, SongInstance, VoteInstance

# Create your views here.
def index(request):

    context = {
        "test": 5,
        "test2": 13,
    }

    # Render the HTML tmeplate index.html with the data in the context variable
    return render(request, "index.html", context=context)

"""
def currentPlaylist(request):


    # Render the HTML tmeplate index.html with the data in the context variable
    return render(request, "currentPlaylist.html", context=context)

def Explore(request):


    # Render the HTML tmeplate index.html with the data in the context variable
    return render(request, "Explore.html", context=context)

def Home(request):

    IP_playlists = pass
    top_100 = pass              #TODO: make the queries
    public_playlists = pass
    profile_information = pass
    playlist_export = pass

    context = {
    "IP_playlists": IP_playlists
    "top_100": top_100
    "public_playlists": public_playlists
    "profile_information": profile_information
    "playlist_export": playlist_export
    }

    # Render the HTML tmeplate index.html with the data in the context variable
    return render(request, "Home.html", context=context)

def myLists(request):


    # Render the HTML tmeplate index.html with the data in the context variable
    return render(request, "myLists.html", context=context)

def playlistSettings(request):


    # Render the HTML tmeplate index.html with the data in the context variable
    return render(request, "playlistSettings.html", context=context)

def profile(request):


    # Render the HTML tmeplate index.html with the data in the context variable
    return render(request, "profile.html", context=context)
    
"""

