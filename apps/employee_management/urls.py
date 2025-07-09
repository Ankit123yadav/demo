from django.urls import path
from . import views

urlpatterns = [
    path('employee_list/', views.employee_list, name='employee_list'),
    path('designation_list/', views.designation_list, name='designation_list'),
    path('add_dummy_designations/', views.add_dummy_designations, name='add_dummy_designations'),
    path('department_list/', views.department_list, name='department_list'),
    path('add_department/', views.add_department, name='add_department'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('attendance/', views.attendance, name='attendance'),
    path('leave_request/', views.leave_request, name='leave_request'),
    path('payroll/', views.payroll, name='payroll'),
    path('holidays/', views.holidays, name='holidays'),
    path('performance_review/', views.performance_review, name='performance_review'),
]