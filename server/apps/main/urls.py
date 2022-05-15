from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from django.urls import path, re_path
from server.apps.main.views import index, FolderCreateViewSet, \
    FileNoteViewSet, SignUp
from . import views
from .views import FolderViewSet, NoteViewSet

app_name = 'main'

router = routers.DefaultRouter()

router.register(r'add/folders', FolderCreateViewSet, 'folders-add')
router.register(r'change/folders', FolderCreateViewSet, 'folders-change')
router.register(r'folders', FolderViewSet, 'folders')
router.register(r'notes', NoteViewSet, 'notes')
router.register(r'files', FileNoteViewSet, 'files')
router.register(r'signup', SignUp, 'signup')

urlpatterns = [
    path('hello/', index, name='hello'),
    re_path(r'^login/', views.login, name='login'),
    re_path(r'logout', views.logout, name='logout'),
    re_path(r'users', views.UserViewSet, name='users'),
    url(r'^admin/', admin.site.urls),

    url(r'', include(router.urls)),
    url(r'^api-auth/', include(
        'rest_framework.urls',
        namespace='rest_framework',
    )),

]
