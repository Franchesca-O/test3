# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-23 00:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20171222_2307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_person', to='users.User')),
                ('shared_with', models.ManyToManyField(related_name='shared', to='users.User')),
            ],
        ),
    ]