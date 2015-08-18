from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^loggedin/$', views.check_user, name="asafa"),
    url(r'^loggedout/$', views.logout_view, name="Log out window"),
	url(r'^load_quiz/$', views.load_quiz, name="Quiz window"),
	url(r'^(?P<quiz_id>\d+)/$', views.load_quiz),
    url(r'^(?P<quiz_id>\d+)/submitquiz$', views.submit_view, name="Result window"),

]		