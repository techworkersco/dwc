# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0015_add_more_verbose_names'),
        ('cms', '0007_auto_20150918_0637'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailSignUpPage',
            fields=[
                ('page_ptr', models.OneToOneField(serialize=False, primary_key=True, auto_created=True, parent_link=True, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterModelOptions(
            name='footercopyblock',
            options={'ordering': ['sort_order'], 'verbose_name': 'Footer Copy Block'},
        ),
    ]
