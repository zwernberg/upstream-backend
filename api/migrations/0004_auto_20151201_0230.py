# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_auto_20151116_0220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('target', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='followers')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='friends')),
            ],
        ),
        migrations.RenameField(
            model_name='catch',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='catch',
            old_name='modified_date',
            new_name='modified_at',
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set([('user', 'target')]),
        ),
    ]
