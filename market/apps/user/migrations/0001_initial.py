# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-20 05:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='my_infor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_name', models.CharField(max_length=11)),
                ('sex', models.IntegerField(choices=[(1, '男'), (2, '女')], default=1)),
                ('my_data', models.DateField(blank=True)),
                ('my_school', models.CharField(max_length=10)),
                ('my_address', models.CharField(max_length=50)),
                ('my_from', models.CharField(blank=True, max_length=50)),
                ('my_tel', models.CharField(max_length=11)),
                ('create_time', models.DateField(auto_now_add=True)),
                ('update_time', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=11)),
                ('password', models.CharField(max_length=32)),
                ('create_time', models.DateField(auto_now_add=True)),
                ('update_time', models.DateField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='my_infor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]
