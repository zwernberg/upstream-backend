# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import stream_django.activity
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catch',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=75)),
                ('fishPhoto', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('likes', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='catches')),
            ],
            bases=(models.Model, stream_django.activity.Activity),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('catch', models.ForeignKey(to='catches.Catch', related_name='liked_users')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set([('user', 'catch')]),
        ),
    ]
