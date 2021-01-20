from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework import generics, permissions, status

from .serializers import (
    QuestionSerializer,
    AnswerSerializer
)

from .models import (
    Question,
    Answer
)


class IsTeacher(permissions.BasePermission):
    """
    Allows access only to teachers.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_staff


class QuestionPostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializers = QuestionSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            x = Question.objects.get(Q_text=serializers.data.get('Q_text'))
            return Response(x.id)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class AnswerPostView(APIView):
    serializer_class = AnswerSerializer
    permission_classes = (IsTeacher,)

    def post(self, request, *args, **kwargs):
        serializers = AnswerSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            x = Answer.objects.get(A_text=serializers.data.get('A_text'))
            return Response(x.id)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class OneQuestionView(APIView):

    def get_answers(self, pk):
        x = Answer.objects.filter(Q_id=pk)
        ans = []
        for i in x:
            y = {
                'answer_text': i.A_text
            }
            ans.append(y)
        return ans

    def get(self, request, pk, format=None):
        x = Question.objects.get(pk=pk)
        # import pdb;pdb.set_trace()
        data = {
            'question_text': x.Q_text,
            'answers': self.get_answers(pk),
            'attachment': x.attachment.url
        }
        return Response(data)
