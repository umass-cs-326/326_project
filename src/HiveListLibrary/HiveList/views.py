from django.shortcuts import render

from HiveList.models import Playlist, Contributors, Artist, Song, Genre, SongInstance

# Create your views here.
def index(request):

    context = {
        "test": 5,
        "test2": 13,
    }

    # Render the HTML tmeplate index.html with the data in the context variable
    return render(request, "index.html", context=context)


def currentPlaylist(request):

    playlist = Playlist.objects.order_by("?").first()
    all_songInstances = SongInstance.objects.filter(playlist_id__exact=playlist.playlist_id).values('song_id')
    all_songs = Song.objects.filter(song_id__in=all_songInstances)
    # Render the HTML tmeplate index.html with the data in the context variable
    context = {
            "songs" : all_songs,
            "current_playlist" : playlist
            }
    return render(request, "currentPlaylist.html", context=context)

def Explore(request):

    playlists = Playlist.objects.all()[:10]
    playlist_ids = Playlist.objects.all()[:10].values('playlist_id')
    all_songInstances = SongInstance.objects.filter(playlist_id__in=playlist_ids).values('song_id')
    songs = Song.objects.filter(song_id__in=all_songInstances)
    context = {
            "popular_playlists" : playlists,
            "popular_songs" : songs,
            }
    # Render the HTML tmeplate index.html with the data in the context variable
    return render(request, "Explore.html", context=context)
"""
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

