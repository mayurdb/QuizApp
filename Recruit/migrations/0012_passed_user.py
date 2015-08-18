# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Recruit', '0011_user_quiz_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passed_User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user1', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
