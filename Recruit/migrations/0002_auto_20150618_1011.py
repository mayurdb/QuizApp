# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recruit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_quiz',
            name='question_bank',
            field=models.ManyToManyField(blank=True, to='Recruit.Parent_text', null=True),
        ),
        migrations.AlterField(
            model_name='parent_text',
            name='parent_text',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
