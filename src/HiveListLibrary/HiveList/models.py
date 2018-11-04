import uuid
from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.urls import reverse

now = datetime.datetime.now()

# Create your models here.


class Playlist(models.Model):
    playlist_id =models.UUIDField(
                               primary_key=True,
                               default=uuid.uuid4,
                               help_text="Unique ID for this particular Playlist across entire site",
                               )
    playlist_name = models.CharField(max_length=200, help_text="Enter a title for the playlist (e.g. Meat Bird Execution Playlist)")
    #User needs to be implemented before foreignKey to user can be used
    #playlist_creator_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    playlist_creation_date = models.DateField(auto_now_add=True, blank=True)
    playlist_description = models.TextField(max_length=1000, help_text="Enter description for playlist")
    #playlist_vote_time = models.DateTimeField(null=True, blank=True)
    playlist_ranking = models.IntegerField(default=0)
    playlist_votingthreshold = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)])
    playlist_is_private = models.BooleanField(default=False)

    """def get_absolute_url(self):
        return reverse("playlist-info", args=[str(self.id)])
    """

    def __str__(self):
        return self.playlist_name


class Contributors(models.Model):
    playlist_id = models.ForeignKey(Playlist, on_delete=models.SET_NULL, null=True)
    #need to users to be implemented first before foreignKey to user can be used
    #contributor_id= models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    """
    def get_absolute_url(self):
        return reverse("contributor-info", args=[str(self.id)])
    """

    def __str__(self):
        return self.contributor_id
        

class Artist(models.Model):

    artist_id = models.UUIDField(
                               primary_key=True,
                               default=uuid.uuid4,
                               help_text="Unique ID for this particular Song across entire site",
                               )
    artist_name = models.CharField(max_length=200)
    """
    def get_absolute_url(self):
        return reverse("artist-info", args=[str(self.id)])
    """
    def __str__(self):
    
        return self.artist_name

class Genre(models.Model):
    

    genre_name = models.CharField(primary_key=True, max_length=200, help_text="Enter a genre for the song (e.g. Swedish Heavy Metal)")

    def __str__(self):
        return genre_name



class Song(models.Model):

    title = models.CharField(max_length=200)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    song_id = models.UUIDField(
                               primary_key=True,
                               default=uuid.uuid4,
                               help_text="Unique ID for this particular Song across entire site",
                               )
    """
    def get_absolute_url(self):
        return reverse("song-info", args=[str(self.id)])
    """

    def __str__(self):
    
        return self.song_id



class SongInstance(models.Model):

    song_id = models.ForeignKey(Song, on_delete=models.SET_NULL, null=True)
    song_instance_id = models.UUIDField(
                               primary_key=True,
                               default=uuid.uuid4,
                               help_text="Unique ID for this particular Song Instance",
                               )
    playlist_id = models.ForeignKey(Playlist, on_delete=models.SET_NULL, null=True)
    #need user first
    #contributor_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    number_yes_votes = models.IntegerField(default=0)
    number_no_votes = models.IntegerField(default=0)

    """
    def get_absolute_url(self):
        return reverse("song-instance-info", args=[str(self.id)])
    """

    def __str__(self):
    
        return self.song_instance_id

"""
class VoteInstance(models.Model):

    contributor_id = models.ForeignKey('Contributor', on_delete=models.SET_NULL, null=True)
    song_id = models.ForeignKey('SongInstance', on_delete=models.SET_NULL, null=True)
    playlist_id = models.ForeignKey('Playlist', on_delete=models.SET_NULL, null=True)
    vote_instance_id = models.UUIDField(primary_key=True,
                                        default=uuid.uuid4,
                                        help_text="unique ID for this particular Song Instance"
                                        )
    VOTE_STATUS = (
      ('y', 'yes'),
      ('n', 'no')
      )

    vote = models.CharField(max_length=1, choices=VOTE_STATUS, blank=True)


    def __str__(self):
        
        return self.vote_instance_id

"""


