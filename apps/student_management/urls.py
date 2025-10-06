from django.urls import path
from . import views

urlpatterns = [
    path('add_user/', views.add_user, name='add_user'),
    path('all_users/', views.all_users, name='all_users'),
    
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('workshop_student/', views.workshop_student, name='workshop_student'),
]