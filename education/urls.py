from django.urls import path
from .views import *

urlpatterns = [
	path('', courses_list, name='courses_list_url'),
	path('archive/', courses_archive, name='courses_archive_url'),
	path('create/', course_create, name='course_create_edit_url'),
	path('<int:course_id>/', course_detail, name='course_detail_url'),
	path('<int:course_id>/edit/', course_edit, name='course_create_edit_url'),
	path('<int:course_id>/delete/', course_delete, name='course_delete_url'),
	path('<str:period>/', courses_filter_by_period, name='courses_filter_by_period_url'),
	path('month/<str:month>/', courses_filter_by_month, name='courses_filter_by_month_url'),
]