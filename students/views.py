from django.shortcuts import render
from django.http import HttpResponse

# Views for Students

def students_list (request):
	return render (request, 'students/students_list.html', {})

def students_add (request):
	return HttpResponse ('<h1>Stud_add_form</h1>')

def students_edit (request, sid):
	return HttpResponse ('<h1>Edit stud %s</h1>' %sid)

def students_delete (request, sid):
	return HttpResponse ('<h1>Delete Stud %s</h1>' %sid)

# Views for Groups

def groups_list (request):
	return HttpResponse ('<h1>groups_list</h1>')

def groups_add (request):
	return HttpResponse ('<h1>Group add form </h1>')

def groups_edit (request, gid):
	return HttpResponse ("<h1>Edit Group %s</h1>" %gid)

def groups_delete (request, gid):
	return HttpResponse ('<h1>Delete Group %s</h1>' % gid)

