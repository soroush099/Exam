from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from exams.models import Exam, Question
from exams.serializers import ExamSerializer, QuestionSerializer, AnswerSerializer


class ListExamView(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer


class DetailExamView(APIView):
    def get(self, request, pk):
        query = Question.objects.filter(exam=pk)
        serializer = QuestionSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnswerSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class CreatExamView(generics.CreateAPIView):
    serializer_class = ExamSerializer


class CreatQuestionView(generics.CreateAPIView):
    serializer_class = QuestionSerializer
