from .models import *
from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.cache import cache_control
from django.template import RequestContext, loader
import random

def index(request):
    template = loader.get_template("Recruit/index.html")
    return HttpResponse(template.render())

@cache_control(no_cache=True, must_revalidate=True)
def check_user(request):
	data = request.POST
	user = authenticate(username=data['username'], password=data['password'])
	quiz_list = []
	if user is not None:
		login(request, user)
		for user in User_profile.objects.all():
			if user.user.username == data['username']:
				quiz_list = user.user_quiz_set.all()
			for quiz in quiz_list:
				quiz.parent_bank.clear()
				quiz.question_bank.clear()
		return render(request, 'Recruit/loggedin.html', {'username' : data['username'], 'quiz_list' : quiz_list})

	else:
		return HttpResponse("Invalid details")

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/Recruit/')

@login_required
@cache_control(no_cache=True, must_revalidate=True)
def load_quiz(request, quiz_id):
	q = get_object_or_404(Quiz, pk=quiz_id)
	user = request.user
	user_profile = user.user_profile
	key = 0
	if q.parent_text_set.all()[0].parent_text == '':
		varlist = q.parent_text_set.all()[0].question_set.all()
	else:
		varlist = q.parent_text_set.all()
		key = 1
	questionset = []
	k = random.sample(range(0, len(varlist)), q.max_question)
	for i in range(0,len(k)):
		questionset.append(varlist[k[i]])
	for j in user_profile.user_quiz_set.all():
		if j.quiz.quiz_name == q.quiz_name:
			if key == 0:
				if j.question_bank.count() == 0 :
					j.question_bank = questionset
					j.save
				qset = j.question_bank.all()
			else:
				if j.parent_bank.count() == 0 :
					j.parent_bank = questionset
					j.save
				qset = j.parent_bank.all()
	return render(request,'Recruit/load_quiz.html', {'quiz' : q, 'varlist' : qset, 'key' : key})

@login_required
@cache_control(no_cache=True, must_revalidate=False)
def submit_view(request, quiz_id):
	q = get_object_or_404(Quiz, pk=quiz_id)
	user =request.user
	user_profile = user.user_profile
	score = 0.0
	quiz_list = []
	for j in user_profile.user_quiz_set.all():  	
		if j.quiz.quiz_name == q.quiz_name:
			if  q.parent_text_set.all()[0].parent_text == '':
				for que in j.question_bank.all() :
					if request.POST.get('%d' % que.id) == 'True':
						score += 1
			else:
				for para in j.parent_bank.all() :
					for que in para.question_set.all():
						if request.POST.get('%d' % que.id) == 'True':
							score += 1
			score = (score *100)/j.quiz.max_question
			if j.score == 0.01: 
				j.score = score
				j.save()
			score = j.score

			if j.score < j.quiz.pass_score:
				result = "You failed " + j.quiz.quiz_name + " quiz. :("
				j.result = False
				j.save()
			else:
				result = "You passed " + j.quiz.quiz_name + " quiz. :)"
				j.result = True
				j.save()

	for j in user_profile.user_quiz_set.all(): 
		if j.score ==0.01:
			quiz_list.append(j)
	key=0
	if len(quiz_list) == 0:
		for j in user_profile.user_quiz_set.all(): 
			if j.result == False:
				key =1
	if key == 0:
		user_profile.passed = True
		user_profile.save()

	return render(request, 'Recruit/submitquiz.html', {'q' : q, 'score' : str(score) + '%', 'quiz_list' : quiz_list, 'result' : result, "key" : key})
