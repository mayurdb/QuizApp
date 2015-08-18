# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recruit', '0005_auto_20150622_0542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_quiz',
            name='score',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
