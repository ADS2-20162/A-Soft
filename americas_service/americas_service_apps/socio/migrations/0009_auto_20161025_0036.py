# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-25 05:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socio', '0008_auto_20161025_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conyuge',
            name='email',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='socio.Email'),
        ),
    ]