from django.contrib import admin

from server.apps.main.models import Folder
from server.apps.main.models import Note

admin.site.register(Note)
admin.site.register(Folder)
