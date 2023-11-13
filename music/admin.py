from django.contrib import admin
from django.contrib import admin

from .models import Genre,Song,Singer,Playlist,Type,Language

# Register your models here.
admin.site.register(Song)
admin.site.register(Singer)
admin.site.register(Genre)
admin.site.register(Playlist)
admin.site.register(Type)
admin.site.register(Language)