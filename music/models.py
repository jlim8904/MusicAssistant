import datetime
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import NullBooleanField
from datetime import date, time

# Create your models here.
class Type(models.Model):
    singer_type = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.singer_type

class Singer(models.Model):
    singer = models.CharField(max_length=20, unique=True)
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.singer

class Genre(models.Model):
    genre = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.genre

class Language(models.Model):
    language = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.language

class Song(models.Model):
    song_name = models.CharField(max_length=30)
    singer = models.ForeignKey('Singer', on_delete=models.SET_NULL, null=True)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre)
    description = models.TextField(max_length=5000, blank=True)
    lyrics = models.TextField(max_length=5000, blank=True)
    website = models.URLField(max_length=2000, blank=True)
    date = models.DateField(default=date.today)
    image = models.CharField(max_length=100, default="aimer.jpg")
    source = models.CharField(max_length=100, default="audio.mp3")
    times_play = models.IntegerField(default=0)

    def __str__(self):
        return self.song_name+" - "+self.singer.singer

class Playlist(models.Model):
    playlist_name = models.CharField(max_length=100)
    song = models.ManyToManyField(Song)
    description = models.TextField(max_length=5000, blank=True)
    times_play = models.IntegerField(default=0)
    image = models.CharField(max_length=100, default="lyricSong.jpg")

    def __str__(self):
        return self.playlist_name