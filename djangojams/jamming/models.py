from django.db import models

class Genre(models.Model):
    id = models.CharField(primary_key=True, max_length=50)

class Album(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

class Artist(models.Model):
    name = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    genre_aff = models.ForeignKey(Genre, on_delete=models.CASCADE)

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Users(models.Model):
    id = models.IntegerField(primary_key=True)

class Playlist(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)

class Artist_Song(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Album_Song(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)

class Genre_Song(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)

class Plays(models.Model):
    amount = models.ForeignKey(Song, on_delete=models.CASCADE)

class User_Playlist(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)

class User_Playlist_Song(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    playlist_id = models.ForeignKey(User_Playlist, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()