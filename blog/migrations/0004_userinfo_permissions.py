# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-09-05 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190905_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='permissions',
            field=models.IntegerField(choices=[(1, '普通用户'), (2, 'vip'), (3, 'vvip')], default=1),
        ),
    ]