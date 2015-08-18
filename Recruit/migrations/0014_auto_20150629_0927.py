# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recruit', '0013_auto_20150629_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_quiz',
            name='parent_bank',
            field=models.ManyToManyField(default=None, to='Recruit.Parent_text', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='user_quiz',
            name='question_bank',
            field=models.ManyToManyField(default=None, to='Recruit.Question', null=True, blank=True),
        ),
    ]
