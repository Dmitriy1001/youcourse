from django.urls import path
from .views import *

urlpatterns = [
	path('', courses_list, name='courses_list_url'),
	path('archive/', courses_archive, name='courses_archive_url'),
	path('create/', course_create, name='course_create_url'),
	path('<int:course_id>/', course_detail, name='course_detail_url'),
	path('<int:course_id>/edit/', course_edit, name='course_edit_url'),
	path('<int:course_id>/delete/', course_delete, name='course_delete_url'),

	path('<str:month>/', courses_filter, name='courses_filter_url'),
]