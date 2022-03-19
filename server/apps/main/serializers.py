import folders as folders
from django.contrib.auth.models import User
from rest_framework import serializers
from server.apps.main.models import Folder, Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"


class FolderSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True)

    class Meta:
        model = Folder
        fields = ["num_user", "name", "release_date", 'notes']


class UserSerializer(serializers.ModelSerializer):
    folders = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='main:folders-detail'
    )

    class Meta:
        model = User
        fields = ["id", "email", "username", "last_name", "first_name", 'folders']  #
