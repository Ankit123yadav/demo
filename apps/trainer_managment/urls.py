from django.urls import path
from . import views

urlpatterns = [
    path('add_trainer/', views.add_trainer, name='add_trainer'),
    path('trainer_list/', views.trainer_list, name='trainer_list'),
    path('schedule/', views.trainer_schedule, name='trainer_schedule'),
    path('feedback/', views.feedback, name='feedback'),
    # Add more URL patterns as needed
]