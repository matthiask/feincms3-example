# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-05 10:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='app_instance_namespace',
            field=models.CharField(default='', editable=False, max_length=100, verbose_name='app instance namespace'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='page',
            name='language_code',
            field=models.CharField(choices=[(b'en', 'English'), (b'de', 'German')], default=b'en', max_length=10, verbose_name='language'),
        ),
    ]