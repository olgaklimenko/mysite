# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo_gallery', '0002_auto_20150809_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
