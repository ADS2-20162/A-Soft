# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-25 04:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('socio', '0004_auto_20161024_2332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conyuge',
            name='email',
        ),
        migrations.RemoveField(
            model_name='socio',
            name='email',
        ),
        migrations.DeleteModel(
            name='Email',
        ),
    ]