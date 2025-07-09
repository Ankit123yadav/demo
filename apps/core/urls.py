from django.urls import path
from . import views

urlpatterns = [
    # path('base/', views.home, name='core-home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.admindashboard, name='admindashboard'),
  
]