# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-09-11 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20190911_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='avatars_default',
            field=models.IntegerField(choices=[(0, '默认头像'), (1, '用户上传头像')], default=0),
        ),
    ]
