from django.urls import path
from . import views 

urlpatterns = [
    path('add_student/', views.add_student, name='add_student'),
    path('student_list/', views.student_list, name='student_list'),
    path('batch/', views.batch, name='batch'),
    path('course/', views.course, name='course'),
    path('student_feedback/', views.student_feedback, name='student_feedback'),
    # Add more URL patterns as needed
]
