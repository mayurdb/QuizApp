# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
                ('is_answer', models.BooleanField()),
                ('var', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Parent_text',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('parent_text', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('parent_text', models.ForeignKey(to='Recruit.Parent_text')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('quiz_name', models.CharField(default='', max_length=32)),
                ('max_question', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='User_profile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_quiz',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('score', models.IntegerField(default=0)),
                ('quiz', models.ForeignKey(to='Recruit.Quiz')),
                ('user_profile', models.ForeignKey(to='Recruit.User_profile')),
            ],
        ),
        migrations.AddField(
            model_name='parent_text',
            name='quiz',
            field=models.ForeignKey(to='Recruit.Quiz'),
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='Recruit.Question'),
        ),
    ]
