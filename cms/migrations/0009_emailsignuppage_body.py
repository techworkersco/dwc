# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0008_auto_20150919_0232'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailsignuppage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(default=''),
        ),
    ]
