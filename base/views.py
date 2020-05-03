from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, logout, update_session_auth_hash
from django.contrib.auth import login
from .models import *

import os

# Create your views here.
valid_extensions = ['mp4', 'mkv', 'avi']


def index(request):

	context = {}
	template_name = 'base/index.html'

	return render(request, template_name, context)


def indexMode2(request):

	path = "C:/Users/seesa02/Desktop/MyData/Entertainment/slix/static/Movies"
	return HttpResponseRedirect('/getFilesAndFolders/%s/' % path)



def getFilesAndFolders(request, path):

	files = []

	if path[-1] != '/':
		path += '/'

	context = {'files': [], 'folders': [], 'srt': [], 'path': path}
	template_name = 'base/getFilesAndFolders.html'
	tempPath = "C:/Users/seesa02/Desktop/MyData/Entertainment/slix/static/"


	for f in os.listdir(path):

		if os.path.isfile(path+f):
			
			if f.endswith('srt'):
				srtName = (str(path+f).split(tempPath))[1]
				context['srt'].append(srtName)

			else:
				for extension in valid_extensions:				
					if f.endswith(extension):
						context['files'].append(f)
		
		else:
			context['folders'].append(f)

	return render(request, template_name, context)


def movies_home(request):

	context = {}
	template_name = 'movie/index.html'
	
	return render(request, template_name, context)



def play_movie(request, movieName):

	path = "C:/Users/seesa02/Desktop/MyData/Entertainment/slix/static/"
	movieName = (str(movieName).split(path))[1]
	srtName = '.'.join(movieName.split('.')[:-1]) + '.srt'

	context = {'movieName': movieName, 'srtName': srtName}
	template_name = 'movie/play_movie.html'
	return render(request, template_name, context)