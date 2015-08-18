# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recruit', '0008_auto_20150624_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_quiz',
            name='score',
            field=models.FloatField(null=True, default=0.01, blank=True),
        ),
    ]
