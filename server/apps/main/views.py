from django.contrib.auth import get_user_model
from requests import Response
from rest_framework import viewsets
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Folder, Note
from server.apps.main.serializers import FolderSerializer, NoteSerializer, UserSerializer

User = get_user_model()


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/index.html')


class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
