from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello, La Franzella kong makulit! This is the public index</h1>")