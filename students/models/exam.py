# -*- coding: utf-8 -*-
from django.db import models


class Exam (models.Model):

	class Meta (object):
		verbose_name = u'Екзамен'
		verbose_name_plural = u'Екзамени'

	subject = models.CharField (
		max_length = 256,
		blank = False,
		verbose_name = u'Назва предмету')

	exam_of_group = models.CharField (
		max_length =256,
		blank = False,
		verbose_name =u'Група, яка екзаменується')

	time = models.DateField (
		blank = False,
		verbose_name = u'Дата і час екзамену',
		null = True)

	teacher_name = models.CharField (
		max_length = 256,
		blank = False,
		verbose_name = u'Екзаменатор')

	def __str__ (self):
		return u"%s %s %s %s" % (self.subject, self.exam_of_group, self.time, self.teacher_name)