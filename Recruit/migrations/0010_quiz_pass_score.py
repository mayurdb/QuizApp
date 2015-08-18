# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recruit', '0009_auto_20150624_0622'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='pass_score',
            field=models.FloatField(default=33),
        ),
    ]
