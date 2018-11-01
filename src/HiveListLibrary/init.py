import textwrap
from datetime import timedelta

# Create a super user to use the admin site.
from django.contrib.auth.models import User
from faker import Faker

from HiveList.models import Genre#Playlist, Contributors, Genre, Song, Artist, SongInstance, VoteInstance

fake = Faker()

# Create Genres
genres = [
    Genre(genre_name="Pop"),
    Genre(genre_name="Hip Hop"),
    Genre(genre_name="Country"),
    Genre(genre_name="Afro"),
    Genre(genre_name="Latin"),
    Genre(genre_name="Electro/EDM"),
    Genre(genre_name="R&B"),
    Genre(genre_name="Rock"),
    Genre(genre_name="Indie"),
    Genre(genre_name="Folk/Acoustic"),
    Genre(genre_name="Classical"),
    Genre(genre_name="Jazz"),
    Genre(genre_name="Party"),
    Genre(genre_name="Christian"),
    Genre(genre_name="Comedy"),
    Genre(genre_name="K-Pop"),
    Genre(genre_name="Reggae"),
    Genre(genre_name="Metal"),
    Genre(genre_name="Soul"),
    Genre(genre_name="Blues"),
    Genre(genre_name="Punk")
]

# Save Genres
for genre in genres:
    genre.save()
"""
# Create Artists
artists = []
a_id = 0
for i in range(1, 100):
    a_name = fake.first_name() + fake.last_name()
    artist = Artist(artist_name = a_name, artist_id = a_id)
    artist.save()
    artists.append(artist)
    a_id += 1

# Create Songs
songs = []
s_id = 0
for i in range(1, 500):
    s_title = fake.text(20)
    s_genre = genres[fake.random_int(0, len(genres)) - 1]
    s_artist = artists[fake.random_int(0, len(genres)) - 1]
    song = Song(title = s_title, genre = s_genre, song_id = s_id, artist = s_artist)
    song.save()
    songs.append(song)
    s_id += 1

# Create Users
users = []
for i in range(1, 200):
    u_fname = fake.first_name()
    u_lname = fake.last_name()
    u_username = fake.text(10)
    user = User(first_name = u_fname, last_name = u_lname, username = u_username)
    user.save()
    users.append(user)

# Create Playlists
playlists = []
p_id = 0
for i in range(1, 50):
    p_name = fake.text(20)
    p_creator = users[fake.random_int(0, len(users)) - 1]
    p_private = fake.boolean()
    p_creation_date = fake.date()
    p_description = fake.text(1000)
    p_vote_time = fake.date_time()
    p_ranking = fake.random_int(0, 100000)
    p_voting_threshold = fake.random_int(1, 101)
    playlist = Playlist(playlist_id = p_id, playlist_name = p_name, playlist_creator = p_creator, playlist_creation_date = p_creation_date, playlist_description = p_description, playlist_is_private = p_private, playlist_vote_time = p_vote_time, playlist_ranking = p_ranking, playlist_votingthreshold = p_voting_threshold)
    playlist.save()
    playlists.append(playlist)
    p_id += 1

# Create Contributors
contributors = []
c_id = 0
for i in range(1, 200):
    playlist_id = playlists[fake.random_int(0, len(playlists)) - 1]
    contributor = Contributor(c_id = contributor_id, playlist_id = playlist_id)
    contributor.save()
    contributors.append(contributor)
    c_id += 1

# Create SongInstances
song_instances = []
si_siid = 0
for i in range(1, 1000):
    si_id = songs[fake.random_int(0, len(songs)) - 1]
    si_playlsit_id = playlists[fake.random_int(0, len(playlists)) - 1]
    si_number_yes_votes = fake.random_int(0, 500)
    si_number_no_votes = fake.random_int(0, 500)
    si_cid = contributors[fake.random_int(0, len(contributors)) - 1]
    song_instance = SongInstance(song_instance_id = si_siid, contributor_id = si_cid, song_id = si_id, playlist_id = si_playlist_id, number_yes_votes = si_number_yes_votes, number_no_votes = si_number_no_votes)
    song_instance.save()
    song_instances.append(song_instance)
    si_siid += 1

# Create VoteInstances
vote_instances = []
votes = ['y', 'yes', 'n', 'no']
vi_viid = 0
for i in range(1, 10000):
    vi_contributor_id = contributors[fake.random_int(0, len(contributors)) - 1]
    vi_song_id = songs[fake.random_int(0, len(songs)) - 1]
    vi_vote = votes[fake.random_int(0, len(votes)) - 1]
    vi_pid = playlists[fake.random_int(0, len(playlists)) - 1]
    vote_instance = VoteInstance(vote_instance_id = vi_viid, playlist_id = vi_pid, contributor_id = vi_contributor_id, song_id = vi_song_id, vote = vi_vote)
    vote_instance.save()
    vote_instances.append(vote_instance)
    vi_viid += 1
"""

#Create SuperUser
username = "admin"
password = "admin"
email = "admin@326.edu"
adminuser = User.objects.create_user(username, email, password)
adminuser.save()
adminuser.is_superuser = True
adminuser.is_staff = True
adminuser.save()
