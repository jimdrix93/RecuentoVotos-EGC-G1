# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Poll(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    start_date = models.DateTimeField
    end_date = models.DateTimeField


class Question(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    optional = models.BooleanField(default=False)
    multiple = models.BooleanField(default=False)
    poll = models.ForeignKey(Poll, null=False, on_delete=models.CASCADE)


class QuestionOption(models.Model):
    description = models.TextField(max_length=200)
    question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE)


class OptionPerVote(models.Model):
    question_option = models.ForeignKey(QuestionOption, on_delete=models.CASCADE)
    vote = models.ForeignKey('Vote', on_delete=models.CASCADE)


VOTE_TYPE = (

        ('0', ' WEB'),
        ('1', 'SLACK'),
        ('2', 'TELEGRAM')
    )


class Vote(models.Model):
    vote_type = models.CharField(max_length=1, choices=VOTE_TYPE)
    vote_date = models.DateTimeField
    token = models.CharField(max_length=50)
    question_options = models.ManyToManyField(QuestionOption, through='OptionPerVote')

class Results(models.Model):
    question_option = models.ForeignKey()
    quantity = models.IntegerField()