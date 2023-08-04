from django.db import models

class Genre(models.Model):
    id = models.CharField(primary_key=True, max_length=50)

class Album(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

class Artist(models.Model):
    name = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)  # An artist can be in multiple genres

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    artists = models.ManyToManyField(Artist)  # A song can have many artists
    genres = models.ManyToManyField(Genre)   # A song can be in multiple genres

class Users(models.Model):
    id = models.IntegerField(primary_key=True)

class Playlist(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    songs = models.ManyToManyField(Song, through='User_Playlist_Song')

class User_Playlist_Song(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()

class Plays(models.Model):
    amount = models.ForeignKey(Song, on_delete=models.CASCADE)