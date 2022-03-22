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
        r_notes = validated_data.pop('notes')
        r_files = validated_data.pop('files')
        folder = Folder.objects.create(**validated_data)
        for r_note in r_notes:
            Note.objects.create(num_folder=folder, **r_note)
        for r_file in r_files:
            FileNote.objects.create(num_folder=folder, **r_file)
        return folder

    def update(self, instance, validated_data):
        note_data = validated_data.pop('notes')
        note = instance.note
        file_data = validated_data.pop('files')
        filenote = instance.filenote

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

        filenote.is_premium_member = file_data.get(
            'is_premium_member',
            filenote.is_premium_member
        )
        filenote.has_support_contract = file_data.get(
            'has_support_contract',
            filenote.has_support_contract
        )
        filenote.save()

        return instance


class UserSerializer(serializers.ModelSerializer):
    folders = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='main:folders-detail'
    )

    class Meta:
        model = User
        fields = ["email", "username", "last_name", "first_name", 'folders']  #
