from django.contrib import admin

from .models import EntryReadActivity, ArtistCheckedActivity, SongCheckedActivity, UserDetailCheckedActivity, GenreCheckedActivity

admin.site.register(EntryReadActivity)
admin.site.register(ArtistCheckedActivity)
admin.site.register(SongCheckedActivity)
admin.site.register(UserDetailCheckedActivity)
admin.site.register(GenreCheckedActivity)