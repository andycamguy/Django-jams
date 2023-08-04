# God I pray this works
# views.py
from rest_framework import viewsets,status
from rest_framework.decorators import action, api_view
from .models import Genre, Album, Artist, Song, Users, Playlist, Plays
from .serializers import *
#================================================
class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    # Genre views
def genre_list(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def genre_detail(request, pk):
    try:
        genre = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GenreSerializer(genre)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#================================================
class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
def album_detail(request, pk):
    try:
        album = Album.objects.get(pk=pk)
    except Album.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AlbumSerializer(album)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AlbumSerializer(album, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        album.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#===================================================
class ArtistViewSet(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    # Artist views
def artist_list(request):
    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def artist_detail(request, pk):
    try:
        artist = Artist.objects.get(pk=pk)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArtistSerializer(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#---------------------------------------------
class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    # Custom action to add a song

    @action(detail=False, methods=['post'])
    def add_song(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # Custom action to remove a song
    @action(detail=True, methods=['delete'])
    def remove_song(self, request, pk=None):
        song = self.get_object()
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Custom action to update a song
    @action(detail=True, methods=['put'])
    def update_song(self, request, pk=None):
        song = self.get_object()
        serializer = self.get_serializer(song, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    # Custom action to read song properties
    @action(detail=True, methods=['get'])
    def song_properties(self, request, pk=None):
        song = self.get_object()
        return Response({
            'name': song.name,
            'album': song.album.name,
            'artist': song.artist.name,
            'genre': song.genre.name
        })
#======================================================
class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
def user_detail(request, pk):
    try:
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#=====================================================
class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
def playlist_list(request):
    if request.method == 'GET':
        playlists = Playlist.objects.all()
        serializer = PlaylistSerializer(playlists, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PlaylistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def playlist_detail(request, pk):
    try:
        playlist = Playlist.objects.get(pk=pk)
    except Playlist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlaylistSerializer(playlist)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PlaylistSerializer(playlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        playlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#-------------------------------------------------------

def song_with_artist_and_genre(request):
    # Perform the join operation using Django's ORM
    songs_with_artist_and_genre = Song.objects.select_related('artist', 'album__genre')

    # Serialize the queryset using the SongSerializer
    serializer = SongSerializer(songs_with_artist_and_genre, many=True)

    return Response(serializer.data)

