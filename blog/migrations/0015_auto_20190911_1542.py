# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-09-11 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20190911_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='avatars',
            field=models.FileField(default='static/default.jpg', upload_to='avatars/', verbose_name='头像'),
        ),
    ]
