from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models import Exam

def exam (request):
	exam = Exam.objects.all()

		# paginate students
	paginator = Paginator(exam, 6)
	page = request.GET.get('page')

	try:
		exam = paginator.page(page)

	except PageNotAnInteger:
		# If page is not integer, deliver first page
		exam = paginator.page(1)

	except EmptyPage:
		# If page is out of range (e. g. 9999), deliver
		# last page of results
		exam = paginator.page(paginator.num_pages)

	return render (request, 'students/exam.html', {'exam': exam})