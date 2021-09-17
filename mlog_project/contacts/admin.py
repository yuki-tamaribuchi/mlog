from django.contrib import admin

from contacts.models import ContactContent, ContactThreads

admin.site.register(ContactContent)
admin.site.register(ContactThreads)