from django.urls import path

from exams.views import *

urlpatterns = [
    path("", ListExamView.as_view()),
    path("<int:pk>/", DetailExamView.as_view(), name='exam_detail'),
    path("create/", CreatExamView.as_view()),
    path("create/question/", CreatQuestionView.as_view()),

]
