from django.shortcuts import render, HttpResponse
from rest_framework import viewsets

# Create your views here.


def index(req):
    return HttpResponse('<h1>Hello, World!</h1>')
