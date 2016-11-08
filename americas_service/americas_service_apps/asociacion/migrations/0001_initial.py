# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-11-08 22:40
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
                ('tipo_cuenta', models.CharField(max_length=50)),
                ('numero_cuenta', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Cuentas de bancos',
                'verbose_name': 'Cuenta de banco',
            },
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('lote', models.CharField(max_length=3, unique=True, verbose_name='ingrese lote')),
                ('area_lote', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='area total')),
                ('estado', models.BooleanField(default=True)),
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
                ('manzana', models.CharField(max_length=3, unique=True, verbose_name='ingrese manzana')),
            ],
            options={
                'verbose_name_plural': 'Manzanas',
                'verbose_name': 'Manzana',
            },
        ),
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
                ('conyuge', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='socio', to='asociacion.Socio')),
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
                ('area_construida', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('estado_inmueble', models.CharField(blank=True, choices=[('Terreno sin construir', 'Terreno sin construir'), ('Terreno con cerco perimetrico', 'Terreno con cerco perimetrico'), ('Inmueble parcialmente construido', 'Inmueble parcialmente construido'), ('Inmueble construido - primera planta', 'Inmueble construido - primera planta'), ('Inmueble construido - segunda planta', 'Inmueble construido - segunda planta'), ('Inmueble construido - más de dos plantas', 'Inmueble construido - más de dos plantas')], max_length=30, null=True)),
                ('observaciones', models.TextField(blank=True, max_length=500, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('lote_socio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='asociacion.Lote')),
                ('socio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asociacion.Socio')),
            ],
            options={
                'verbose_name_plural': 'Relacion de socio a lotes',
                'verbose_name': 'Relacion de socio a lote',
            },
        ),
    ]
