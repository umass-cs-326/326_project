from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    #path("songs/", views.SongListView.as_view(), name="songs"),
    #path("song/<int:pk>", views.SongDetailView.as_view(), name="song-detail"),
]

