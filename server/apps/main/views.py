from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from rest_framework import viewsets
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views.decorators.http import require_http_methods
from django.contrib import auth
from .models import Folder, Note, FileNote
from server.apps.main.serializers import FolderSerializer, NoteSerializer, \
    UserSerializer, FolderCreateSerializer, FileNoteSerializer, \
    RegistrationSerializer

User = get_user_model()
pkU = 'olga'


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
    permission_classes = (AllowAny,)
    queryset = User.objects.all().filter(username=pkU)
    serializer_class = UserSerializer


class SignUp(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer


@require_http_methods(['GET', 'POST'])
def login(request):
    username = request.GET.get('username', '')
    password = request.GET.get('password', '')
    pkU = User.objects.all().filter(username=username, password=password)
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        print("Авторизация проходит без проблем!")
        auth.login(request, user)
        return HttpResponse(user)
    else:
        print("Ой, что-то пошло не так!")
        return HttpResponse("Ой, что-то пошло не так!")


def logout(request):
    auth.logout(request)
    return HttpResponse("Success")
