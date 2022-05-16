from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework import viewsets
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.views.decorators.http import require_http_methods
from django.contrib import auth

import config
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


@require_http_methods(['GET', 'POST'])
def UserViewSet(request):
    username = request.GET.get('username', '')
    user = User.objects.all().filter(username=username)
    if user is not None:
        serializer = UserSerializer(user, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse(serializer.errors, status=404)


class SignUp(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class=RegistrationSerializer


@require_http_methods(['GET', 'POST'])
def login(request):
    username = request.GET.get('username', '')
    password = request.GET.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        print("Авторизация проходит без проблем!")
        auth.login(request, user)
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=404)


def logout(request):
    auth.logout(request)
    return HttpResponse("Success")
