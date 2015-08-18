from django.contrib import admin
from .models import *

class Parent_textInline(admin.StackedInline):
	model = Parent_text

class QuizAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['quiz_name']}),
		(None,               {'fields': ['max_question']}),
		(None,               {'fields': ['pass_score']}),
	]
	inlines = [Parent_textInline]

admin.site.register(Quiz, QuizAdmin)

class QuestionInline(admin.StackedInline):
	model = Question

class Parent_textAdmin(admin.ModelAdmin):
	fields = ['parent_text']
	inlines = [QuestionInline]

admin.site.register(Parent_text, Parent_textAdmin)

class ChoiceInline(admin.StackedInline):
	model = Choice
  
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)

class User_quizInline(admin.TabularInline):
	model = User_quiz
	fields = ['quiz', 'score', 'result']

class User_profileAdmin(admin.ModelAdmin):
	list_display = ('name', 'passed')
	inlines = [User_quizInline]

admin.site.register(User_profile, User_profileAdmin)
