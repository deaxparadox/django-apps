from typing import Any

from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import get_list_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    # def get_queryset(self) -> QuerySet[Any]:
    #     return Question.objects.order_by("-pub_date")[:5]
    
    def get_queryset(self) -> QuerySet[Any]:
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :5
        ]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

