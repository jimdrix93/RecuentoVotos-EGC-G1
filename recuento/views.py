# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, JsonResponse
from models import Question, Poll
from serializers import QuestionSerializer
import loadpoll
import CountMethods

def index(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        poll = Poll.objects.get(pk=pk)
    except Poll.DoesNotExist:
        try:
            loadpoll.loadpoll(pk)
        except :
            return HttpResponse(status=404)
    try:
        CountMethods.approvecount(pk)
        questions = Question.objects.filter(poll=pk)
    except Question.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = QuestionSerializer(questions, many=True)
        return JsonResponse(serializer.data, safe=False)
    else :
        return HttpResponse(status=400)