# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20171128_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_group',
            field=models.ForeignKey(verbose_name='Група', null=True, on_delete=django.db.models.deletion.PROTECT, to='students.Group'),
        ),
    ]
