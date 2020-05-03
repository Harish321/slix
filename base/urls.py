from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
	
	url('^$', views.indexMode2, name='index'),
	url('^getFilesAndFolders/(?P<path>.+)$', views.getFilesAndFolders, name='getFilesAndFolders'),

	url('^play_movie/(?P<movieName>.+)$', views.play_movie, name='play_movie'),

]