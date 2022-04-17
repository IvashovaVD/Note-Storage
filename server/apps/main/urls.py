from django.conf.urls import url, include
from django.contrib.auth.views import LogoutView
from rest_framework import routers
from django.urls import path
from server.apps.main.views import index, UserViewSet, FolderCreateViewSet, \
    FileNoteViewSet, LoginView, SignUp, LogoutView
from .views import FolderViewSet, NoteViewSet


app_name = 'main'

router = routers.DefaultRouter()

router.register(r'add/folders', FolderCreateViewSet, 'folders-add')
router.register(r'change/folders', FolderCreateViewSet, 'folders')
router.register(r'folders', FolderViewSet, 'no-reg-user')
router.register(r'notes', NoteViewSet, 'notes')
router.register(r'files', FileNoteViewSet, 'files')
router.register(r'users', UserViewSet, 'users')
router.register(r'login', LoginView, 'login')
router.register(r'signup', SignUp, 'signup')
router.register(r'logout', LogoutView, 'logout')

urlpatterns = [
    path('hello/', index, name='hello'),

    url(r'', include(router.urls)),
    url(r'^api-auth/', include(
        'rest_framework.urls',
        namespace='rest_framework',
    ),
        )
]
