# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_homepage_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderLinkSnippet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('url', models.URLField()),
                ('text', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
                'ordering': ['sort_order'],
            },
        ),
    ]
