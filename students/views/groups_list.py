from django.shortcuts import render
from django.http import HttpResponse

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