# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-03 16:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(max_length=500)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
        ),
        migrations.AddField(
            model_name='asistencia',
            name='evento',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='eventos.Evento'),
            preserve_default=False,
        ),
    ]
