from django.contrib import admin

from .models import EntryReadActivity, ArtistCheckedActivity, SongCheckedActivity, UserDetailCheckedActivity

admin.site.register(EntryReadActivity)
admin.site.register(ArtistCheckedActivity)
admin.site.register(SongCheckedActivity)
admin.site.register(UserDetailCheckedActivity)