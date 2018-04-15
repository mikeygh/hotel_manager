# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-13 01:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('num_rooms', models.IntegerField(default=0)),
                ('overbook_level', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('guest_name', models.CharField(blank=True, default=b'', max_length=100)),
                ('guest_email', models.CharField(blank=True, default=b'', max_length=100)),
                ('arrival_date', models.DateTimeField(default=b'')),
                ('departure_date', models.DateTimeField(default=b'')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]