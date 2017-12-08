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

	def __str__ (self):
		return u'%s %s' % (self.student_name)