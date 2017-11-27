from django.shortcuts import render
from django.http import HttpResponse

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