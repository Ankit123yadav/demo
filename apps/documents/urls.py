from django.urls import path
from . import views

urlpatterns = [
    path('upload_certificate/', views.upload_certificate, name='upload_certificate'),
]
