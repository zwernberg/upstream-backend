# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import stream_django.activity
import taggit.managers
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Catch',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=75)),
                ('location', models.CharField(max_length=75)),
                ('fishPhoto', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('length', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('likes', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='catches')),
                ('tags', taggit.managers.TaggableManager(through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags', help_text='A comma-separated list of tags.')),
            ],
            bases=(models.Model, stream_django.activity.Activity),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
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
