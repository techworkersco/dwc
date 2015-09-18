# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_auto_20150917_0922'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterCopyBlock',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('body', wagtail.wagtailcore.fields.RichTextField(default='')),
                ('sort_order', models.IntegerField(default=9999)),
            ],
            options={
                'verbose_name': 'Header Link',
                'ordering': ['sort_order'],
            },
        ),
        migrations.CreateModel(
            name='FooterLink',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('url', models.CharField(max_length=2048)),
                ('text', models.CharField(max_length=255)),
                ('sort_order', models.IntegerField(default=9999)),
            ],
            options={
                'verbose_name': 'Footer Link',
                'ordering': ['sort_order'],
            },
        ),
        migrations.AlterModelOptions(
            name='headerlink',
            options={'verbose_name': 'Header Link', 'ordering': ['sort_order']},
        ),
    ]
