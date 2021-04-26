from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required

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

def courses_filter(request, month):
	courses = [course for course in Course.objects.all()\
			   if month in course.start.ctime()]
	context = utils.pagination(request, utils.relevant_filter(courses), 6)
	return render(request, 'education/courses_list.html', context)

def courses_archive(request):
	courses = Course.objects.all()
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
	page = utils.what_page_on_paginator(request, 6, course_id)
	if request.method == 'POST':
		course.delete()
		return redirect(f'../../?page={page}')
	return render(request, 'education/course_delete.html', {'course': course})


	 

									