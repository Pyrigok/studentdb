# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_student_student_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('data', models.DateField(verbose_name='Дата', null=True)),
                ('student_name', models.ForeignKey(verbose_name='Студент', null=True, on_delete=django.db.models.deletion.PROTECT, to='students.Student')),
            ],
            options={
                'verbose_name': 'Відвідування',
                'verbose_name_plural': 'Відвідування',
            },
        ),
    ]
