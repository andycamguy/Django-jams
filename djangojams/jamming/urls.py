from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
router = DefaultRouter()
router.register(r'genres', GenreViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'artists', ArtistViewSet)
router.register(r'songs', SongViewSet)
router.register(r'users', UsersViewSet)
router.register(r'playlists', PlaylistViewSet)



urlpatterns = [
    path('', include(router.urls)),
]