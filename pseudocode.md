# What am I doing?
Description
Create a music library database/API with Django using this template(Docker) as a base for a local project. Gitpod Template
 For this project, we will be setting up a Python/Django/Django REST Framework API app,
 creating models that can be migrated into the database from a reference to a DB Diagram to serve
 as the backend for an application like Spotify or Apple Music.
Ports served: 
 - PostgresQL DB: 5432 (automatic)
 - Django server: 8000 (when running  manage.py runserver )


# Questions
## What is a song and what are its properties and methods?
-it is music
- it is part of an album
- a song is part of a genre
- written by an artist or artists

## what is an album?
- it is a collection of music
- a collection of songs
- a part of a genre
- written by an artist or artists
## what is a genre?
- a collection of music
- a collection of songs
- a collection of albums
- can be pieces of an album(s) for the actual entity or concept
- written by artists

## what is a musical artist?
- makes music
- composes a song
- is a part of a genre or multiple genres(or affilition with the genre)
- works along with other artists to make songs
- works along with other artists for making albums

# User Stories
- as a listener I wish to see a display of my music so that I know which songs are played by a certain artist
- as a listener I wish to have access of my music so I can listen to Spotify at any time(for the purposes of this project I don't need to provide audio files)
- as a user I wish to make playlists of my own so I can pick and choose songs of my greatest desires for the best music vibes

# Procedural
## Begin

## Init
 - Punch the tables into the database
 - start up postgresql
 - install django
 - install djangorestframework
 - freeze >requirements.txt
 - add the CORS FILE FROM THE READ.ME
   - connect views in the app
   - connect views in the project
   - set up models in the app. don't forget to make migrations and migrate when they are made.
     
 
## Models

### Song
  id integer
  name varchar
  album_id integer
  artist_id varchar

### Album
id varchar 
genre_id varchar
### Artist
  name varchar
  album varchar
  genre_aff varchar

### Genre
id varchar
### User
  id integer 

### Playlist
  user_id varchar
  label varchar
### Plays
  amount fk 
## Views
# End
# Functional

# OOP / Models / Thinking in Django REST 
## My diagram
https://dbdiagram.io/d/64b8589302bd1c4a5e5e4752
