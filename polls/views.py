from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from .models import Question
from django.template import loader
# Create your views here.

def index(request):
    question_list= Question.objects.order_by('-pub_date')[:3]
    context= {
        'latest_question_list' : question_list
    }
    return render(request, 'polls/index.html', context)

def details(request, question_id):
    question= get_object_or_404(Question, pk= question_id)
    return render(request, 'polls/details.html', {'question': question})

def results(request, question_id):
    return HttpResponse('results for id '+ str(question_id))

def votes(request, question_id):
    return HttpResponse('votes for id '+ str(question_id))