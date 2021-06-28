from django.contrib import admin

from .models import EntryReadActivity, ArtistCheckedActivity, SongCheckedActivity

admin.site.register(EntryReadActivity)
admin.site.register(ArtistCheckedActivity)
admin.site.register(SongCheckedActivity)