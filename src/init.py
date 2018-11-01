import textwrap
from datetime import timedelta

# Create a super user to use the admin site.
from django.contrib.auth.models import User
from faker import Faker

from HiveList.models import Playlist, PlaylistContributors, Users, Genre, Songs, Artist, SongInstance, VoteInstance

fake = Faker()

# Create Genres
genres = [
    Genre(name="Pop"),
    Genre(name="Hip Hop"),
    Genre(name="Country"),
    Genre(name="Afro"),
    Genre(name="Latin"),
    Genre(name="Electro/EDM"),
    Genre(name="R&B"),
    Genre(name="Rock"),
    Genre(name="Indie"),
    Genre(name="Folk/Acoustic"),
    Genre(name="Classical"),
    Genre(name="Jazz"),
    Genre(name="Party"),
    Genre(name="Christian"),
    Genre(name="Comedy"),
    Genre(name="K-Pop"),
    Genre(name="Reggae"),
    Genre(name="Metal"),
    Genre(name="Soul"),
    Genre(name="Blues"),
    Genre(name="Punk")
]

# Save Genres
for genre in genres:
    genre.save()

# Create Artists
artists = []
a_id = 0
for i in range(1, 100):
    a_fname = fake.first_name()
    a_lname = fake.last_name()
    artist = Artist(fname = a_fname, lname = a_lname, artid = a_id)
    artist.save()
    artists.append(artist)
    a_id += 1

# Create Songs
songs = []
s_id = 0
for i in range(1, 500):
    s_name = fake.text(20)
    s_genre = genres[fake.random_int(0, len(genres)) - 1]
    song = Song(name = s_name, genre = s_genre, songid = s_id)
    song.save()
    songs.append(song)
    s_id += 1

# Create Users
users = []
u_id = 0
for i in range(1, 200):
    u_fname = fake.first_name()
    u_lname = fake.last_name()
    u_username = fake.text(10)
    user = User(fname = u_fname, lname = u_lname, username = u_username, userid = u_id)
    user.save()
    users.append(user)
    u_id += 1

# Create Playlists
playlists = []
p_id = 0
for i in range(0, 50):
    p_name = fake.text(20)
    p_creator_id = users[fake.random_int(0, len(users)) - 1]
    p_private = fake.boolean()
    p_creation_date = fake.date()
    p_description = fake.text(1000)
    playlist = Playlist(playlist_id = p_id, playlist_name = p_name, playlist_creator_id = p_creator_id, playlist_creation_date = p_creation_date, playlist_description = p_description, playlist_is_private = p_private)
    playlist.save()
    playlists.append(playlist)
    p_id += 1

# Create Contributors
contributors = []
c_id = 0
for i in range(1, 200):
    c_playlist_id = playlists[fake.random_int(0, len(playlists)) - 1]
    contributor = Contributor(c_id = contributor_id, c_playlist_id = contributor_playlist_id)
    contributor.save()
    contributors.append(contributor)
    c_id += 1

# Create SongInstances
song_instances = []
for i in range(1, 1000):
    si_id = songs[fake.random_int(0, len(songs)) - 1]
    si_playlsit_id = playlists[fake.random_int(0, len(playlists)) - 1]
    si_score = fake.random_int(0, 100)
    song_instance = SongInstance(song_id = si_id, playlist_id = si_playlist_id, score = si_score)
    song_instance.save()
    song_instances.append(song_instance)

# Create VoteInstances
vote_instances = []
votes = ['y', 'yes', 'n', 'no']
for i in range(1, 10000):
    vi_contributor_id = contributors[fake.random_int(0, len(contributors)) - 1]
    vi_song_id = songs[fake.random_int(0, len(songs)) - 1]
    vi_vote = votes[fake.random_int(0, len(votes)) - 1]
    vote_instance = VoteInstance(contributor_id = vi_contributor_id, song_id = vi_song_id, vote = vi_vote)
    vote_instance.save()
    vote_instances.append(vote_instance)

