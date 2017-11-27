from django.shortcuts import render
from django.http import HttpResponse

def journal (request):
	journal = (
		{'id': 1,
		'name': u'Василь Пиріг'},
		{'id': 2,
		'name': u'Христина Пиріг'}
		)
	return render (request, 'students/journal.html', {'journal': journal})