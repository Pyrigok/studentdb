from django.shortcuts import render
from django.http import HttpResponse

# Views for Students

def students_list (request):
	students = (
			{'id':1,
			'first_name': u'Христина',
			'last_name': u'Пиріг',
			'ticket': 235,
			'image': 'img/Khrs.jpg'},

			{'id': 2,
			'first_name': u'Пиріг',
			'last_name': u'Христинка',
			'ticket': 564,
			'image': 'img/Khrs.jpg'}
		)
	return render (request, 'students/students_list.html',
				{'students': students})

def students_add (request):
	return HttpResponse ('<h1>Stud_add_form</h1>')

def students_edit (request, sid):
	return HttpResponse ('<h1>Edit stud %s</h1>' %sid)

def students_delete (request, sid):
	return HttpResponse ('<h1>Delete Stud %s</h1>' %sid)

# Views for Groups

def groups_list (request):
	groups = (
		{'id': 1,
		'name': u'МтС-31',
		'leader': u'Христина Бочкай'},
		{'id': 2,
		'name': u'МтС-32',
		'leader': u'Ігор Залізний'}
		)
	return render (request, 'students/groups_list.html', {'groups': groups})

def groups_add (request):
	return HttpResponse ('<h1>Group add form </h1>')

def groups_edit (request, gid):
	return HttpResponse ("<h1>Edit Group %s</h1>" %gid)

def groups_delete (request, gid):
	return HttpResponse ('<h1>Delete Group %s</h1>' % gid)

