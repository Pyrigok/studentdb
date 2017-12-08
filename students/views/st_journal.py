from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models import Journal

def journal (request):
	journal = Journal.objects.all()

	# paginate students
	paginator = Paginator(journal, 11)
	page = request.GET.get('page')

	try:
		journal = paginator.page(page)

	except PageNotAnInteger:
		# If page is not integer, deliver first page
		journal = paginator.page(1)

	except EmptyPage:
		# If page is out of range (e. g. 9999), deliver
		# last page of results
		journal = paginator.page(paginator.num_pages)


	return render (request, 'students/journal.html', {'journal': journal})