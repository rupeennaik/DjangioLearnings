from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello World. You are at polls index")


def home(request):
    return HttpResponse ("You are at home page")


def newpoll(request):
    return HttpResponse ("This is a new poll")
