from django.urls import path
from .views import (
    QuestionPostView,
    AnswerPostView,
    OneQuestionView
)

urlpatterns = [
    path('question/', QuestionPostView.as_view(), name="post_question"),
    path('writeanswer/', AnswerPostView.as_view(), name="post_answer"),
    path('question/<int:pk>/', OneQuestionView.as_view(), name='single_question')
]
