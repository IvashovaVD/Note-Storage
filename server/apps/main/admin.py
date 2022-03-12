from django.contrib import admin

from server.apps.main.models import Folder
from server.apps.main.models import Note


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin):
    class Meta:
        model = Folder


class NoteAdmin(admin.ModelAdmin):
    class Meta:
        model = Note


admin.site.register(Note, NoteAdmin)

