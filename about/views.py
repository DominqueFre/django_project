from django.shortcuts import render
# # this is the default import for views.py, but we won't
# be using it in this simple example.

from django.http import HttpResponse
# Create your views here.


def about_me(request):
    return HttpResponse("This would be the about page.")
