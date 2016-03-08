# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('target', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='followers')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='friends')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set([('user', 'target')]),
        ),
    ]
