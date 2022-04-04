from django.conf.urls import url, include
from django.contrib.auth.views import LogoutView
from rest_framework import routers
from django.urls import path
from server.apps.main.views import index, UserViewSet, FolderCreateViewSet, \
    FileNoteViewSet
from . import views
from .views import FolderViewSet, NoteViewSet


app_name = 'main'

router = routers.DefaultRouter()

router.register(r'add/folders', FolderCreateViewSet, 'folders-add')
router.register(r'change/folders', FolderCreateViewSet, 'folders')
router.register(r'folders', FolderViewSet, 'no-reg-user')
router.register(r'notes', NoteViewSet, 'notes')
router.register(r'files', FileNoteViewSet, 'files')
router.register(r'users', UserViewSet, 'users')

urlpatterns = [
    path('hello/', index, name='hello'),
    path("signup", views.SignUp.as_view(), name="signup"),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout$', LogoutView.as_view(), name='logout'),

    url(r'', include(router.urls)),
    url(r'^api-auth/', include(
        'rest_framework.urls',
        namespace='rest_framework',
    ),
        )
]
