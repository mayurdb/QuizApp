from django.db import models
from django.contrib.auth.models import User

class User_profile(models.Model):
	user = models.OneToOneField(User)
	passed = models.BooleanField(default=False)
	def __str__(self):
		return self.user.username
	def name(self):
		return self.user.username


class Quiz(models.Model):
	quiz_name = models.CharField(max_length=32, default="")
	max_question = models.IntegerField(default=1)
	pass_score = models.FloatField(default=33)
	def __str__(self):
		return self.quiz_name
	

class User_quiz(models.Model):
	user_profile = models.ForeignKey(User_profile)
	quiz = models.ForeignKey(Quiz)
	score = models.FloatField(default=0.01 ,blank=True, null=True)
	result = models.BooleanField(default=False)
	parent_bank = models.ManyToManyField('Parent_text', default = None, blank=True, null=True)
	question_bank = models.ManyToManyField('Question', default = None, blank=True, null=True)
	def __str__(self):
		return self.user_profile.user.username + " " + self.quiz.quiz_name


class Parent_text(models.Model):
	quiz = models.ForeignKey(Quiz)
	parent_text = models.CharField(max_length=2000, blank=True, null=True)
	def __str__(self):
		return self.parent_text

class Question(models.Model):
	parent_text = models.ForeignKey(Parent_text)
	question_text = models.CharField(max_length=200)
	def __str__(self):
		return self.question_text

class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	is_answer = models.BooleanField()
	def __str__(self):
		return self.choice_text
