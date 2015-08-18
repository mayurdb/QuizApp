# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recruit', '0004_remove_choice_var'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_quiz',
            name='score',
            field=models.IntegerField(blank=True),
        ),
    ]
