from rest_framework import serializers

from exams.models import Exam, Question, Answer


class ExamSerializer(serializers.ModelSerializer):
    # question = QuestionSerializer()
    class Meta:
        model = Exam
        fields = ('id', 'title', 'description', 'category', 'grade',
                  'curse_name', 'sources', 'difficulty_level',
                  'starting_date', 'end_date', 'negative_point',
                  'auther', 'is_enable',
                  )


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('question', 'option1', 'option2', 'option3', 'option4',
                  'suggested_time', 'score', 'level', 'exam'
                  )


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"
