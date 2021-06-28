from django.contrib import admin

from .models import EntryReadActivity, ArtistCheckedActivity

admin.site.register(EntryReadActivity)
admin.site.register(ArtistCheckedActivity)