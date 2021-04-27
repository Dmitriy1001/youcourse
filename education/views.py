from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Course
from . import utils
# Create your views here.

def courses_list(request):
	search = request.GET.get('search', '')
	if search:
		courses = Course.objects.filter(Q(name__contains=search))
	else:	
		courses = Course.objects.all()
	context = utils.pagination(request, utils.relevant_filter(courses), 6)
	return render(request, 'education/courses_list.html', context)

def courses_filter_by_month(request, month):
	courses = [course for course in Course.objects.all()\
			   if month in course.start.ctime()]
	context = utils.pagination(request, utils.relevant_filter(courses), 6)
	return render(request, 'education/courses_list.html', context)

def courses_filter_by_period(request, period):
	courses = Course.objects.all()
	d = {
		'year': filter(lambda x: x.start.year==timezone.now().year, courses),
		'month': filter(lambda x: x.start.month==timezone.now().month, courses),
		'week': filter(
				lambda x: x.start.isocalendar()[1]==timezone.now().isocalendar()[1], 
				courses)
	}
	courses = list(d[period])
	context = utils.pagination(request, utils.relevant_filter(courses), 6)
	return render(request, 'education/courses_list.html', context)


def courses_archive(request):
	courses = Course.objects.order_by('-start')
	relevant_courses = utils.relevant_filter(courses)
	courses = [course for course in courses if course not in relevant_courses]
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


	 

									