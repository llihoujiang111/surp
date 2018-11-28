# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-28 07:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20181123_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateField(auto_now_add=True, verbose_name='创建')),
                ('update_time', models.DateField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='假删除')),
                ('hcity', models.CharField(max_length=20, verbose_name='省')),
                ('hproper', models.CharField(max_length=20, verbose_name='市')),
                ('harea', models.CharField(blank=True, max_length=20, null=True, verbose_name='区')),
                ('add_name', models.CharField(max_length=11, verbose_name='收货人')),
                ('add_tel', models.CharField(max_length=11, verbose_name='收货电话')),
                ('add_detailed', models.CharField(max_length=255, verbose_name='详细地址')),
                ('isdefault', models.BooleanField(default=False, verbose_name='默认选中')),
                ('infor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.my_infor', verbose_name='用户信息id')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='用户id')),
            ],
            options={
                'verbose_name': '收货地址',
                'verbose_name_plural': '收货地址',
            },
        ),
    ]
