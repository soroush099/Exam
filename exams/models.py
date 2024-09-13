from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from profiles.models import CustomUser


# Create your models here.


class GeneralCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("name"))
    category_type = models.CharField(max_length=255, verbose_name=_("type"))
    description = models.CharField(max_length=400, verbose_name=_("description"))

    class Meta:
        verbose_name = _("GeneralCategory")
        verbose_name_plural = _("GeneralCategories")

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("name"))
    description = models.CharField(max_length=400, verbose_name=_("description"))
    general_category = models.ForeignKey(GeneralCategory, on_delete=models.CASCADE, verbose_name=_("general category"))

    class Meta:
        verbose_name = _("SubCategory")
        verbose_name_plural = _("SubCategories")

    def __str__(self):
        return self.name


class Exam(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("title"))
    description = models.TextField(verbose_name=_("description"))
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, verbose_name=_("category"))
    grade = models.CharField(max_length=255, verbose_name=_("grade"))
    curse_name = models.CharField(max_length=255, verbose_name=_("curse name"))
    sources = models.CharField(max_length=255, verbose_name=_("sources"))
    difficulty_level = models.CharField(max_length=255, verbose_name=_("difficulty level"))
    starting_date = models.DateTimeField(verbose_name=_("start date"))
    end_date = models.DateTimeField(verbose_name=_("end date"))
    negative_point = models.BooleanField(default=False, verbose_name=_("negative point"))
    auther = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  on_delete=models.SET_NULL, null=True, verbose_name=_("auther"), related_name="auther")
    is_enable = models.BooleanField(default=False, verbose_name=_("is enable"))
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=_("created time"))
    updated_time = models.DateTimeField(auto_now=True, verbose_name=_("updated time"))

    class Meta:
        verbose_name = _("exam")
        verbose_name_plural = _("exams")

    def __str__(self):
        return self.title


class Question(models.Model):
    question = models.CharField(max_length=255, verbose_name=_("question"))
    option1 = models.CharField(max_length=255, verbose_name=_("option1"))
    option2 = models.CharField(max_length=255, verbose_name=_("option2"))
    option3 = models.CharField(max_length=255, verbose_name=_("option3"))
    option4 = models.CharField(max_length=255, verbose_name=_("option4"))
    right_option = models.CharField(max_length=255, verbose_name=_("right option"))
    suggested_time = models.TimeField(verbose_name=_("time"))
    score = models.IntegerField(verbose_name=_("score"))
    level = models.CharField(max_length=255, verbose_name=_("level"))
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, verbose_name=_("exam"))
    is_enable = models.BooleanField(default=False, verbose_name=_("is enable"))
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=_("crated time"))
    updated_time = models.DateTimeField(auto_now=True, verbose_name=_("updated time"))

    class Meta:
        verbose_name = _("question")
        verbose_name_plural = _("questions")

    def __str__(self):
        return self.question


class Answer(models.Model):
    exam_id = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    selection_option = models.CharField(max_length=10)

