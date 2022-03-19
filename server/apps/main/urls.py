from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path
from server.apps.main.views import index, UserViewSet
from .views import FolderViewSet, NoteViewSet

app_name = 'main'

router = routers.DefaultRouter()

router.register(r'folders', FolderViewSet, 'folders')
router.register(r'notes', NoteViewSet, 'notes')
router.register(r'users', UserViewSet, 'users')

urlpatterns = [
    path('hello/', index, name='hello'),
    url(r'', include(router.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
