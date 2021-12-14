import re

from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import CourseCreateEditForm
from .models import Course


def relevant_filter(courses):
    for course in courses:
        if course.start < timezone.now() < course.end:
            course.start = 'Курс розпочався'
        elif timezone.now() > course.end:
            course.start = 'Курс завершено'
    return list(filter(lambda course: course.start != 'Курс завершено', courses))


def months_list():
    '''Only months with relevant courses are listed'''
    eng_ua = {
        "Dec": "Грудень", "Jan": "Січень", "Feb": "Лютий",
        "Mar": "Березень", "Apr": "Квітень", "May": "Травень",
        "Jun": "Червень", "Jul": "Липень", "Aug": "Серпень",
        "Sep": "Вересень", "Oct": "Жовтень", "Nov": "Листопад",
    }
    months = []
    for course in Course.objects.all():
        if timezone.now() < course.end:
            month = re.search(r'\w+\s+(\w+)\s+\w+', course.start.ctime()).group(1)
            month = (eng_ua[month], month)
            if month not in months:
                months.append(month)
    return months


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
        'months': months_list(),
        'page': page,
        'is_paginated': is_paginated,
        'prev_url': prev_url,
        'next_url': next_url
    }


def what_page_on_paginator(request, objs_on_page, course_id, archived=False):
    if archived:
        courses = Course.objects.filter(end__lt=timezone.now())
    else:
        courses = Course.objects.filter(end__gt=timezone.now())

    pages, page, count = {}, 1, 0
    for course in courses:
        if count == objs_on_page:
            page += 1
            count = 0
        pages[course] = page
        count += 1
    course = get_object_or_404(Course, id=course_id)
    return pages[course]


# mixins

def create_edit_course(request, action='create', course_id=None):
    if action == 'edit':
        course = get_object_or_404(Course, id=course_id)
    if request.method == 'POST':
        if action == 'edit':
            form = CourseCreateEditForm(
                request.POST, request.FILES,
                instance=course,
            )
        else:
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
