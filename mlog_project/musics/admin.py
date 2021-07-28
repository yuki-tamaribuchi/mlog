from django.contrib import admin

from .models import Song, Artist, Genre, BelongTo

admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(BelongTo)