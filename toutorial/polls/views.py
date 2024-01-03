from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from . import models
from django.urls import reverse
from django.template import loader
# Create your views here.

def  index (request):
    lates_question_list = models.Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list" : lates_question_list,
    }
    return render(request, "index.html", context)

def detail (request, question_id):
    question = get_object_or_404(models.Question, pk = question_id)
    return render(request, "detail.html", {"question" : question})

def vote(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(models.Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, models.Choice.DoesNotExist):
        return render(request, "detail.html",{"question": question, "error_message" : "you didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:result", args=(question.id,)))

def results(request, question_id):
    question = get_object_or_404(models.Question, pk = question_id)
    return render(request, "results.html", {"question" : question})