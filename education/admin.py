from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Course


@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):
	list_display = ('name', 'lectures_number', 'start', 'end')
	list_filter = ('lectures_number', 'start', 'end')
	search_fields = ('name',)
	date_hierarchy = 'start'
	summernote_fields = ('text',)
