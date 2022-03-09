from django.contrib import admin

from server.apps.main.models import Folder
from server.apps.main.models import Note


@admin.register(Folder)
class FolderAdmin(admin.ModelAdmin[Folder]):
    """"""


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin[Note]):
    """"""
