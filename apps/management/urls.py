from django.urls import path
from . import views

urlpatterns = [
 path("certificate/", views.certifiicate, name="certificate"),
]