# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-10 14:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asociacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dni_representante', models.CharField(blank=True, max_length=8, null=True)),
                ('fecha', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Asistencias',
                'verbose_name': 'Asistencia',
            },
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(blank=True, max_length=500, null=True)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
            ],
            options={
                'verbose_name_plural': 'Eventos',
                'verbose_name': 'Evento',
            },
        ),
        migrations.CreateModel(
            name='Inasistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('monto', models.CharField(choices=[('10', '10'), ('20', '20'), ('50', '50')], max_length=2)),
                ('num_inasistencias', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Inasistencias',
                'verbose_name': 'Inasistencia',
            },
        ),
        migrations.AddField(
            model_name='asistencia',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eventos.Evento'),
        ),
        migrations.AddField(
            model_name='asistencia',
            name='socio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asociacion.SocioLote'),
        ),
    ]
