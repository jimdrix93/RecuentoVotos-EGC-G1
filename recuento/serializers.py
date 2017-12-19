from rest_framework import serializers
from models import Result, Question, QuestionOption

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = ('quantity',)
        

class QuestionOptionSerializer(serializers.ModelSerializer):
    result = ResultSerializer()
    class Meta:
        model = QuestionOption
        fields = ('description', 'result')

class QuestionSerializer(serializers.ModelSerializer):
    questionoption_set = QuestionOptionSerializer(many=True)
    class Meta:
        model = Question
        fields = ('title', 'description', 'optional', 'multiple', 'questionoption_set')
        depth = 5