from django.urls import path

from .views import QuizListView, QuestionListView

urlpatterns = [
    path('', QuizListView.as_view(), name='quiz-list'),
    path('question/<int:pk>/', QuestionListView.as_view(), name='question-list'),
]