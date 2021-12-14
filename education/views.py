from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from . import utils
from .models import Course


def courses_list(request):
	search = request.GET.get('search', '')
	if search:
		courses = Course.objects.filter(Q(name__contains=search))
	else:	
		courses = Course.objects.all()
	context = utils.pagination(request, utils.relevant_filter(courses), 6)
	return render(request, 'education/courses_list.html', context)

def courses_filter_by_month(request, month_name):
	months = {
		"Dec": 12, "Jan": 1, "Feb": 2,
		"Mar": 3, "Apr": 4, "May": 5,
		"Jun": 6, "Jul": 7, "Aug": 8,
		"Sep": 9, "Oct": 10, "Nov": 10,
	}
	try:
		month_number = months[month_name]
	except KeyError:
		raise Http404('Такого місяця не існує')
	courses = Course.objects.filter(start__month=month_number)
	context = utils.pagination(request, utils.relevant_filter(courses), 6)
	return render(request, 'education/courses_list.html', context)

def courses_filter_by_period(request, period):
	courses = Course.objects.all()
	periods = {
		'year': filter(lambda x: x.start.year == timezone.now().year, courses),
		'month': filter(lambda x: x.start.month == timezone.now().month, courses),
		'week': filter(
				lambda x: x.start.isocalendar()[1] == timezone.now().isocalendar()[1],
				courses,
		)
	}
	try:
		courses = list(periods[period])
	except KeyError:
		raise Http404
	context = utils.pagination(request, utils.relevant_filter(courses), 6)
	return render(request, 'education/courses_list.html', context)


def courses_archive(request):
	courses = Course.objects.filter(end__lt=timezone.now()).order_by('-start')
	context = utils.pagination(request, courses, 6)
	return render(request, 'education/courses_list.html', context)


def course_detail(request, course_id):
	course = get_object_or_404(Course, id=course_id)
	return render(request, 'education/course_detail.html', {'course': course})


@login_required
def course_create(request):
	return utils.create_edit_course(request, 'create')


@login_required
def course_edit(request, course_id):
	return utils.create_edit_course(request, 'edit', course_id)


@login_required
def course_delete(request, course_id):
	course = get_object_or_404(Course, id=course_id)
	archived = timezone.now() > course.end
	page = utils.what_page_on_paginator(request, 6, course_id, archived=archived)
	if archived:
		redirect_url = f'../../archive/?page={page}'
	else:
		redirect_url = f'../../?page={page}'
	if request.method == 'POST':
		course.delete()
		return redirect(redirect_url)
	return render(request, 'education/course_delete.html', {'course': course})




									
