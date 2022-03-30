from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import View
from django.views.generic import TemplateView
from rest_framework import viewsets
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.reverse import reverse

from .models import Folder, Note, FileNote
from server.apps.main.serializers import FolderSerializer, NoteSerializer, UserSerializer, FolderCreateSerializer, \
    FileNoteSerializer, RegistrationSerializer

User = get_user_model()


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/index.html')


class FolderViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


class FolderCreateViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Folder.objects.all()
    serializer_class = FolderCreateSerializer


class NoteViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class FileNoteViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = FileNote.objects.all()
    serializer_class = FileNoteSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RegistrationAPIView(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer


class SignUp(View):
    def get(self, request):
        return render(request, 'signup.html', {'form': UserCreationForm()})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('index'))

        return render(request, 'signup.html', {'form': form})


class LoginView(View):
    def get(self, request):
        return render(request, 'main/login.html', {'form': AuthenticationForm()})

    def post(self, request):
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            return redirect(reverse('index'))

        return render(request, 'signup.html', {'form': form})
