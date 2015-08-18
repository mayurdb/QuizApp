# [QuizApp](http://127.0.0.1/QuizApp)

QuizApp is a sleek, intuitive, and powerful online test application which you can run on any server.



## Table of contents

- [Requirements]
- [Setup]
- [Running]
- [Admin]
- [User]

## Requirements

Minimum Requirements

- Python 2.7
- Django 1.8.2
- Apache Server with mod_wsgi
- Django-admin-tools==0.5.2
- Django-debug-toolbar==1.2.2


## Installation

-Python comes preinstalled on most Linux distributions, and is available as a package on all others.
-If not download (HTTP): https://www.python.org/ftp/python/2.7.10/Python-2.7.10.tar.xz

-Django official releases have a version number, such as 1.4.2, 1.4.1 or 1.4, and the latest one is 
 always available at http://www.djangoproject.com/download/.
-After package downloaded run following commands.

    >$ tar xzvf Django-1.4.2.tar.gz
    >$ cd Django-*
    >$ sudo python setup.py install
 
-Apache download (HTTP): http://httpd.apache.org/download.cgi#apache24
-Run following commands
	 >$ tar xvf httpd-NN.tar
	 >$ cd httpd-NN
	 >$ ./configure --prefix=PREFIX
	 >$ make
	 >$ make install
	 >$ vi PREFIX/conf/httpd.conf
	 >$ PREFIX/bin/apachectl -k start

## Running QuizApp Steps

-Go to terminal run following commands
     >$ cd (path to your QuizAppRoot)
     >$ python manage.py makemigrations
     >$ python manage.py migrate
     >$ python manage.py runserver

-Now your quiz is running
-Open browser type url (HTTP): http://127.0.0.1:8000/admin/
-Hit enter You will be asked admin username and password.
-Default admin name is "admin" and password is "1".


## Admin  

-Admin page contains following titles

Groups 
Users
Parent text 
Questions
Quizs
User Profiles

Users -> add users here 

Groups -> optional field to add users to group

Questions and Parent_text -> to add questions first create parent text then add questions to it.

Quizs -> create quizs here then add related parent text to it.

User_profiles -> create user profiles and assign quiz to user.

-admin can analyze quiz results.
-admin can set limit to display of questions.
-admin can set a passing criteria.

## User

-Open browser type url (HTTP): http://127.0.0.1:8000/Recruit/
-Hit enter You will be asked  username and password.
-enter username and password.
-Begin quiz




 
