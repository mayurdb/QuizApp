# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recruit', '0003_auto_20150620_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='var',
        ),
    ]
