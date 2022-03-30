from abc import ABC, ABCMeta

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from server.apps.main.models import Folder, Note, FileNote


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"


class FileNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileNote
        fields = "__all__"


class FolderSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True)
    files = FileNoteSerializer(many=True)

    class Meta:
        model = Folder
        fields = ["num_user", "name", "release_date", 'notes', 'files']


class FolderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    folders = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='main:folders-detail'
    )

    class Meta:
        model = User
        fields = ["email", "username", "last_name", "first_name", 'folders']  #


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ["email", "username", 'password']
