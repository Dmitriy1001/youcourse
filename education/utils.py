from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Course
from .forms import CourseCreateEditForm

def pagination(request, objs, objs_on_page):
	paginator = Paginator(objs, objs_on_page)
	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)
	is_paginated = page.has_other_pages()

	if page.has_previous():
		prev_url = f'?page={page.previous_page_number()}'
	else:
		prev_url = ''
	if page.has_next():
		next_url = f'?page={page.next_page_number()}'
	else:
		next_url = ''

	return {
		'page': page,
		'is_paginated': is_paginated,
		'prev_url': prev_url,
		'next_url': next_url
	}


def what_page_on_paginator(request, objs_on_page, course_id):
	courses = Course.objects.all()	
	d = {}
	page, count = 1, 0
	for i in courses:
		if count == objs_on_page:
			page += 1; count = 0
		d[i] = page; count += 1
	course = get_object_or_404(Course, id=course_id)
	return d[course]


def create_edit_course(request, action='create', course_id=None):
	if action == 'edit':
		course = get_object_or_404(Course, id=course_id)
	if request.method == 'POST':
		form = CourseCreateEditForm(request.POST, request.FILES)
		if form.is_valid():
			course_obj = form.save()
			return redirect('course_detail_url', course_obj.id)
	else:
		if action == 'create':
			form = CourseCreateEditForm()
		else:	  
			form = CourseCreateEditForm(instance=course)
	return render(request, 'education/course_create_edit.html', {'form': form})					