# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Назва', max_length=256)),
                ('notes', models.TextField(verbose_name='Додаткові нотатки', blank=True)),
            ],
            options={
                'verbose_name': 'Група',
                'verbose_name_plural': 'Групи',
            },
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Студент', 'verbose_name_plural': 'Студенти'},
        ),
        migrations.AddField(
            model_name='group',
            name='leader',
            field=models.OneToOneField(verbose_name='Староста', blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.Student'),
        ),
    ]
