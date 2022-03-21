from django.contrib.auth.models import User
from rest_framework import serializers
from server.apps.main.models import Folder, Note, FileNote


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        exclude = ('id', 'num_folder')


class FileNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileNote
        exclude = ('id', 'num_folder')


class FolderSerializer(serializers.ModelSerializer):
    notes = NoteSerializer(many=True)
    files = FileNoteSerializer(many=True)

    class Meta:
        model = Folder
        fields = ["name", "release_date", 'notes', 'files']

    def create(self, validated_data):
        note_data = validated_data.pop('notes')
        folder = Folder.objects.create(**validated_data)
        Note.objects.create(num_folder=folder, **note_data)
        file_data = validated_data.pop('files')
        FileNote.objects.create(num_folder=folder, **file_data)
        return folder

    def update(self, instance, validated_data):
        note_data = validated_data.pop('notes')
        note = instance.note

        instance.name = validated_data.get('name', instance.name)
        instance.num_user = validated_data.get('num_user', instance.num_user_date)
        instance.save()

        note.is_premium_member = note_data.get(
            'is_premium_member',
            note.is_premium_member
        )
        note.has_support_contract = note_data.get(
            'has_support_contract',
            note.has_support_contract
        )
        note.save()

        return instance


class UserSerializer(serializers.ModelSerializer):
    folders = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='main:folders-detail'
    )

    class Meta:
        model = User
        fields = ["email", "username", "last_name", "first_name", 'folders']  #
