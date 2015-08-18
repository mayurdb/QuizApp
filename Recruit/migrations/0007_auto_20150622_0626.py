# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recruit', '0006_auto_20150622_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_quiz',
            name='score',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
    ]
