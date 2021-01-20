from rest_framework import serializers
from .models import (
    Question,
    Answer,
)


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = [
            'Q_text',
            'user',
            'date',
            'attachment'
        ]


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'A_text',
            'Q_id',
            'user',
        ]
