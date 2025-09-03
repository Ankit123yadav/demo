from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("registration/", views.registration, name="registration"),
    path("apprenticeship/", views.apprenticeship, name="apprenticeship"),
    path("carrer/", views.carrer, name="carrer"),
    path("contactus/", views.contactus, name="contactus"),
    path("courses/", views.courses, name="courses"),
    path("ceme/", views.ceme, name="ceme"),
    path("digital/", views.digital, name="digital"),
    path("eeec/", views.eeec, name="eeec"),
    path("csit/", views.csit, name="csit"),
    path("expert/", views.expert, name="expert"),
    path("industrials/", views.industrials, name="industrials"),
    path("semgallery/", views.semgallery, name="semgallery"),
    path("software/", views.software, name="software"),
    path("mobile/", views.mobile, name="mobile"),
    path("website/", views.website, name="website"),
    path("winter/", views.winter, name="winter"),
    path("teamgallery/", views.teamgallery, name="teamgallery"),
    path("verified/", views.verified, name="verified"),
    path("syllabus/", views.syllabus, name="syllabus"),
    path("all_courses/", views.all_courses, name="all_courses"),
    path("python/", views.python, name="python"),  # New URL for Python course page
    path("demo/", views.demo, name="demo"),  # New URL for demo page
    path("download_certificate/", views.download_certificate, name="download_certificate"),  # New URL for downloading certificate
    path("digital_marketing/", views.digital_marketing, name="digital_marketing"),  # New URL for Digital Marketing course page
    path("android/", views.android, name="android"),  # New URL for Android course page 
    path("mern/", views.mern, name="mern"),  # New URL for MERN course page
    # Add any other URLs as needed
    

]