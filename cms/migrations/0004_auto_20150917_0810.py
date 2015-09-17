# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_headerlinksnippet'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HeaderLinkSnippet',
            new_name='HeaderLink',
        ),
    ]
