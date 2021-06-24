from django.contrib import admin
from .models import Genre,SubGenre,Artist,Song,Entry,Like,Comment,ReadHistory

admin.site.register(Genre)
admin.site.register(SubGenre)
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Entry)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(ReadHistory)