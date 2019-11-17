from django.http import HttpResponse, Http404
# Create your views here.
from .models import Question
from django.template import loader
from django.shortcuts import get_object_or_404, render

def index(request):
    question_list = Question.objects.order_by('publication_date')
    context = {
        'question_list': question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
