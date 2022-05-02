from django.contrib.auth import get_user_model
from django.views import View
from rest_framework import viewsets
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Folder, Note, FileNote
from server.apps.main.serializers import FolderSerializer, NoteSerializer, \
    UserSerializer, FolderCreateSerializer, FileNoteSerializer, \
    RegistrationSerializer

User = get_user_model()


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/index.html')


class FolderViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


class FolderCreateViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Folder.objects.all()
    serializer_class = FolderCreateSerializer


class NoteViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class FileNoteViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = FileNote.objects.all()
    serializer_class = FileNoteSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SignUp(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer


class LoginView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer


class LogoutView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
