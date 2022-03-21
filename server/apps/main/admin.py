from django.contrib import admin

from server.apps.main.models import Folder, FileNote
from server.apps.main.models import Note

admin.site.register(Note)
admin.site.register(Folder)
admin.site.register(FileNote)
