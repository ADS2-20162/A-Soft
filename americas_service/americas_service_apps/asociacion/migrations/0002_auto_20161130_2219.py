# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 03:19
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
        migrations.AddField(
            model_name='socio',
            name='persona',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auths.Person'),
        ),
        migrations.AddField(
            model_name='lote',
            name='manzana',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asociacion.Manzana'),
        ),
        migrations.AddField(
            model_name='asociacion',
            name='cuenta_banco',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='asociaciones', to='asociacion.CuentaBanco'),
        ),
    ]
