# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20150917_0810'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='headerlink',
            options={'verbose_name': 'Header Link'},
        ),
        migrations.AlterField(
            model_name='headerlink',
            name='url',
            field=models.CharField(max_length=2048),
        ),
    ]
