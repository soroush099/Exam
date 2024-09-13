from django.contrib import admin

from .models import Exam, Question, GeneralCategory, SubCategory


# Register your models here.


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ("title", "grade", "curse_name", "sources", "is_enable",
                    "difficulty_level", "negative_point",)
    list_filter = ("grade", "is_enable", "difficulty_level")
    search_fields = ("title", "description", "curse_name", "source", "auther")
    # filter_horizontal = None
    # inlines = None


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("exam", "question", "right_option", "suggested_time", "score", "level", "is_enable",)
    list_filter = ("is_enable", "level")
    search_fields = ("exam", "question")


@admin.register(GeneralCategory)
class GeneralCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "category_type")
    list_filter = ("category_type", )
    search_fields = ("name", "category_type", "description")


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "general_category")
    list_filter = ("general_category", )
    search_fields = ("name", "general_category", "description")
