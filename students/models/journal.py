# -*- coding: utf-8 -*-
from django.db import models

class Journal (models.Model):
	"""Journal Model"""

	class Meta (object):
		verbose_name = u'Відвідування'
		verbose_name_plural = u'Відвідування'

	student_name = models.OneToOneField ('Student',
		verbose_name = u'Студент',
		blank = False,
		null = True,
		on_delete = models.PROTECT)

	data = models.DateField (
		blank = False,
		null = True,
		verbose_name = u'Дата')

	def __str__ (self):
		return u'%s %s' % (self.student_name, self.data)