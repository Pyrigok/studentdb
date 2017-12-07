# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_journal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('subject', models.CharField(verbose_name='Назва предмету', max_length=256)),
                ('exam_of_group', models.CharField(verbose_name='Група, яка екзаменується', max_length=256)),
                ('time', models.DateField(verbose_name='Дата і час екзамену', null=True)),
                ('teacher_name', models.CharField(verbose_name='Екзаменатор', max_length=256)),
            ],
            options={
                'verbose_name': 'Екзамен',
                'verbose_name_plural': 'Екзамени',
            },
        ),
    ]
