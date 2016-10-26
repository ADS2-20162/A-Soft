# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-26 12:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaLote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_construida', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='area construida')),
                ('area_sin_construir', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='area sin construir')),
                ('observaciones', models.TextField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name_plural': 'AreaLotes',
                'verbose_name': 'AreaLote',
            },
        ),
        migrations.CreateModel(
            name='Asociacion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ruc', models.CharField(max_length=11, unique=True, verbose_name='ruc')),
                ('nombre', models.CharField(max_length=100, verbose_name='nombre asociacion')),
                ('denominacion', models.CharField(max_length=150, null=True, verbose_name='denominacion asociacion')),
                ('website', models.URLField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('update_at', models.DateTimeField(auto_now=True, null=True, verbose_name='update at')),
            ],
            options={
                'verbose_name_plural': 'asociaciones',
                'verbose_name': 'asociacion',
            },
        ),
        migrations.CreateModel(
            name='CuentaBanco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entidad_bancaria', models.CharField(max_length=50, unique=True)),
                ('tipo_cuenta', models.CharField(max_length=30)),
                ('numero_cuenta', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'CuentaBancos',
                'verbose_name': 'CuentaBanco',
            },
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('input_lote', models.CharField(max_length=3, unique=True, verbose_name='ingrese lote')),
                ('lote', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asociacion', to='asociacion.Lote')),
            ],
            options={
                'verbose_name_plural': 'Lotes',
                'verbose_name': 'Lote',
            },
        ),
        migrations.CreateModel(
            name='Manzana',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('input_manzana', models.CharField(max_length=3, unique=True, verbose_name='ingrese manzana')),
                ('manzana', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asociacion', to='asociacion.Manzana')),
            ],
            options={
                'verbose_name_plural': 'Manzanas',
                'verbose_name': 'Manzana',
            },
        ),
        migrations.CreateModel(
            name='RelacionManzana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asociacion.Lote')),
                ('manzana', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='asociacion.Manzana')),
            ],
            options={
                'verbose_name_plural': 'RelacionManzanas',
                'verbose_name': 'RelacionManzana',
            },
        ),
        migrations.AddField(
            model_name='asociacion',
            name='cuenta_banco',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asociacion.CuentaBanco'),
        ),
    ]
