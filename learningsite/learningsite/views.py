import os

from django.shortcuts import render
from django.conf import settings


def index(request,path):
	if request.method == 'GET':
		return render(request,os.path.join(settings.STATIC_ROOT,'weibo/index.html'))
