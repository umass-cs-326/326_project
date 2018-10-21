from django.db import models

# Create your models here.


class Playlist(models.Model):
    """
    Model representing a playlist
    """
    playlist_id = models.IntegerField(max_length=100, primary_key=True)
    playlist_name = models.CharField(max_length=200, help_text="Enter a title for the playlist (e.g. Meat Bird Execution Playlist)")
    playlist_creation_date = models.DateField()
    playlist_description = models.TextField(max_length=1000, help_text="Enter description for playlist")

    def __str__(self):
        """
        Description: String for representing the model object (in Admin site etc.)
        :return: the playlist name
        """
        return self.playlist_name


class Contributors(models.Model):
    """
    Model representing all the contributors for a playlist. This will use a playlist ID as a key to the playlists table, and a user ID
    that is a key to the users table
    """
    playlist_id = models.ForeignKey(playlist_id, ondelete=cascade)
    contributor_id = contributor_id = models.ForeignKey(User, ondelete=models.cascade)

    def __str__(self):
        """
        Description:
        :return:
        """
        return self.contributor_id


class Artist(models.Model):
    """
    Model representing a Song
    """
    pass

    def __str__(self):
        """
        Description:
        :return:
        """
        pass


class Song(models.Model):
    """
    Model representing a Song
    """
    pass

    def __str__(self):
        """
        Description:
        :return:
        """
        pass


class Genre(models.Model):
    """
    Model representing a Song
    """
    pass

    def __str__(self):
        """
        Description:
        :return:
        """
        pass


class SongInstance(models.Model):
    """
    Model representing a Song
    """
    pass

    def __str__(self):
        """
        Description:
        :return:
        """
        pass


class VoteInstance(models.Model):
    """
    Model representing a vote
    """
    contributor_id = models.ForeignKey(User, ondelete=models.cascade)
    song_id = models.ForeignKey('SongInstance', ondelete=models.cascade)

    VOTE_STATUS = (
    	('y', 'yes'),
    	('n', 'no')
    	)

    vote = models.CharField(max_length=1, choices=VOTE_STATUS, blank=true)


    def __str__(self):
        """
        Description:
        :return:
        """
        return contributor_id




