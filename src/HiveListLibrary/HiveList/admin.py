from django.contrib import admin

from HiveList.models import Playlist, Contributors, Artist, Song, Genre, SongInstance, VoteInstance

# Register your models here.

@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    #displays
    pass


@admin.register(Contributors)
class ContributorAdmin(admin.ModelAdmin):
    #displays
    pass


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    #displays
    pass


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    #displays
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    #displays
    pass


@admin.register(SongInstance)
class SongInstanceAdmin(admin.ModelAdmin):
    #displays
    pass


@admin.register(VoteInstance)
class VoteInstanceAdmin(admin.ModelAdmin):
    #displays
    pass

