# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-09-11 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20190907_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='avatar',
            field=models.FileField(default='avatars_default/default.jpg', upload_to='avatars/', verbose_name='头像'),
        ),
    ]
