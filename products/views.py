from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Hello world !'
                        'how are you?')


def new(request):
    return HttpResponse('.. https://github.com/django/django.git. You can also download a gzipped tarball of the development version. This archive is updated every time we commit code.')


