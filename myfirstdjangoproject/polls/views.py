from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello World. You are at polls index")


def home(request):
    return HttpResponse ("You are at home page")


def newpoll(request):
    return HttpResponse ("This is a new poll")


def detail(request, question_id):
    return HttpResponse("You are looking at Question %s." % question_id )

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
