from django.shortcuts import render
from django.http import HttpResponse
from .models import Genre,Song,Singer,Playlist,Type,Language

# def index(request):
#     songList = Song.objects.all()

#     return render(request, 'music/index.html', context= {'songList': songList})

def musicView(request):
    songList = Song.objects.all()
    playlist = Playlist.objects.all()

    return render(request, 'music/musicweb.html', context={'song_list': songList, 'playlists': playlist})

def categoryView(request):
    return render(request, 'music/category.html', {})

def listView(request):
    return render(request, 'music/mySongList.html', {})

def playView(request):
    return render(request, 'music/play.html', {})

def searchView(request):
    return render(request, 'music/search.html', {})

def statView(request):
    return render(request, 'music/statistics.html', {})

def profileView(request):
    return render(request, 'music/profile.html', {})

def recommendView(request):
    return render(request, 'music/recommendList.html', {})
    
def settingView(request):
    return render(request, 'music/set.html', {})
