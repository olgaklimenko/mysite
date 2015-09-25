# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import photo_gallery.fields


class Migration(migrations.Migration):

    dependencies = [
        ('photo_gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=photo_gallery.fields.ThumbnailImageField(upload_to=b'photos'),
        ),
    ]
