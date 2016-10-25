# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-25 04:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socio', '0003_auto_20161024_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Emails',
                'verbose_name': 'Email',
            },
        ),
        migrations.AlterField(
            model_name='conyuge',
            name='email',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='socio.Email'),
        ),
        migrations.AlterField(
            model_name='socio',
            name='email',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='socio.Email'),
        ),
    ]