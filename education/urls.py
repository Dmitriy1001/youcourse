from django.urls import path

from . import views


urlpatterns = [
    path('', views.courses_list, name='courses_list_url'),
    path('archive/', views.courses_archive, name='courses_archive_url'),
    path('create/', views.course_create, name='course_create_edit_url'),
    path('<int:course_id>/', views.course_detail, name='course_detail_url'),
    path('<int:course_id>/edit/', views.course_edit, name='course_create_edit_url'),
    path('<int:course_id>/delete/', views.course_delete, name='course_delete_url'),
    path('<str:period>/', views.courses_filter_by_period, name='courses_filter_by_period_url'),
    path('month/<str:month_name>/', views.courses_filter_by_month, name='courses_filter_by_month_url'),
]
