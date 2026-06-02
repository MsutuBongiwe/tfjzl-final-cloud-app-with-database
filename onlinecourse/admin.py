from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5

# This inline allows you to add answer choices directly inside the question form layout
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['content', 'course', 'grade']

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

# Register all models so they appear in your administration portal tables
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)