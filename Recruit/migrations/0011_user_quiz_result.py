# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recruit', '0010_quiz_pass_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_quiz',
            name='result',
            field=models.BooleanField(default=False),
        ),
    ]
