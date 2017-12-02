# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-26 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('w3kun', '0003_auto_20171119_1648'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='Dscrb',
        ),
        migrations.RemoveField(
            model_name='author',
            name='friends',
        ),
        migrations.AddField(
            model_name='article',
            name='time',
            field=models.DateTimeField(auto_now=True, verbose_name='最后修改日期'),
        ),
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]