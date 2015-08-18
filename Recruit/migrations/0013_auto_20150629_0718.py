# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recruit', '0012_passed_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passed_user',
            name='user1',
        ),
        migrations.AddField(
            model_name='user_profile',
            name='passed',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Passed_User',
        ),
    ]
