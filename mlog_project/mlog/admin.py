from django.contrib import admin
from .models import Genre,Artist,Song,Entry,ReadHistory,ArtistCheckedHistory,FavoriteArtist

admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Entry)
admin.site.register(ReadHistory)
admin.site.register(ArtistCheckedHistory)
admin.site.register(FavoriteArtist)