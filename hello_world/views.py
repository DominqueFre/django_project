# from django.shortcuts import render
# # this is the default import for views.py, but we won't
# be using it in this simple example.

from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hello, world!")
