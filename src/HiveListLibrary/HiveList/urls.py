from django.urls import path
from HiveList import views


urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.Home, name="home"),
    path("explore/", views.Explore, name="explore"),
    path("mylists/", views.myLists, name="mylists"),
    path("profile/", views.profile, name="profile"),
    path("currentPlaylist/", views.currentPlaylist, name="currentPlaylist"),
    path("playlistSettings/", views.playlistSettings, name="playlistSettings"),
]

