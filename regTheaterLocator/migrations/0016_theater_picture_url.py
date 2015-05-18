# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regTheaterLocator', '0015_auto_20150518_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='theater',
            name='picture_url',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
