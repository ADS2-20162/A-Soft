# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-28 01:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auths', '0001_initial'),
        ('asociacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_civil', models.CharField(choices=[('Soltero', 'Soltero'), ('Casado', 'Casado'), ('Viudo', 'Viudo'), ('Divorsiado', 'Divorsiado')], max_length=20)),
                ('domicilio', models.CharField(blank=True, max_length=300, null=True)),
                ('procedencia', models.CharField(blank=True, max_length=50, null=True)),
                ('celular', models.CharField(blank=True, max_length=30, null=True)),
                ('telefono', models.CharField(blank=True, max_length=30, null=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('residencia_juliaca', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=2)),
                ('is_adventista', models.CharField(choices=[('Si', 'Si'), ('No', 'No')], max_length=2)),
                ('estado', models.BooleanField(default=True)),
                ('conyuge', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='socio', to='socio.Socio')),
                ('persona', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auths.Person')),
            ],
            options={
                'verbose_name_plural': 'Socios',
                'verbose_name': 'Socio',
            },
        ),
        migrations.CreateModel(
            name='SocioLote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('socio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socio.Socio')),
                ('socio_lote', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='asociacion.RelacionManzana')),
            ],
            options={
                'verbose_name_plural': 'SocioLotes',
                'verbose_name': 'SocioLote',
            },
        ),
    ]
