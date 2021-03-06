# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 08:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('w3kun', '0002_auto_20171116_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='author',
            name='article',
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author', to='w3kun.Author'),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(default='Title', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='friends',
            field=models.ManyToManyField(related_name='_author_friends_+', to='w3kun.Author'),
        ),
        migrations.AddField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article', to='w3kun.Article'),
        ),
        migrations.AddField(
            model_name='comment',
            name='writer',
            field=models.ManyToManyField(related_name='writer', to='w3kun.Author'),
        ),
    ]
