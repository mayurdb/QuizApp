# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recruit', '0002_auto_20150618_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_quiz',
            name='parent_bank',
            field=models.ManyToManyField(to='Recruit.Parent_text', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='user_quiz',
            name='question_bank',
            field=models.ManyToManyField(to='Recruit.Question', null=True, blank=True),
        ),
    ]
