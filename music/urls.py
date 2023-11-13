from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.musicView, name='musicweb'),
    path('category/', views.categoryView, name='category'),
    path('list/', views.listView, name='mySongList'),
    path('play/', views.playView, name='play'),
    path('search/', views.searchView, name='search'),
    path('stat/', views.statView, name='statistics'),
    path('profile/', views.profileView, name='profile'),
    path('recommend/', views.recommendView, name='recommendList'),
    path('setting/', views.settingView, name='set'),
]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.STATIC_URL)
