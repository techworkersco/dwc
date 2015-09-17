# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0005_auto_20150917_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headerlink',
            name='sort_order',
            field=models.IntegerField(default=9999),
        ),
    ]
