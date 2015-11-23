from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'weibo/index.html')


def home(request):
    return render(request, 'home.html')


def test(request):
    enstring = "Testing the sting function for django"
    Tlist = ['Python', 'Django', 'WARC', 'Docker']
    Tdict = {'Li':'90', 'Mi':'80', 'To':'70'}
    return render(request, 'test.html',  {'Tlist': Tlist, 'string': enstring, 'Tdict': Tdict})


def invalid(request, path):

    return render(request, '404.html', {'string': path})
