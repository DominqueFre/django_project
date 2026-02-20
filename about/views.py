from django.shortcuts import render
# # this is the default import for views.py

# from django.http import HttpResponse

# Create your views here.


def about_me(request):
    return render(request, 'index.html')
