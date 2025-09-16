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
    path("asp_net/", views.asp_net, name="asp_net"),  # New URL for ASP.NET course page
    path("iot/", views.iot, name="iot"),  # New URL for IoT
    path("autocad/", views.autocad, name="autocad"),  # New URL for AutoCAD course page
    path("cybersecurity/", views.cybersecurity, name="cybersecurity"),  # New URL for Cyber Security course page
    path("automation/", views.automation, name="automation"),  # New URL for Automation course page
    path("pcb/", views.pcb, name="pcb"),  # New URL for PCB course page
    path("plc/", views.plc, name="plc"),
    path("data_science/", views.data_science, name="data_science"),  # New URL for Data Science course page
    path("ecad/", views.ecad, name="ecad"),  # New URL for ECAD course page
    path("3DMax/", views.D3max, name="3DMax"),  # New URL for 3DMax course page
    path("plumbing/", views.plumbing, name="plumbing"),  # New URL for Plumbing course page
    path("hvac/", views.hvac, name="hvac"),  # New URL for HVAC course page
    path("embedded/", views.embedded, name="embedded"),  # New URL for Embedded Systems course page
    path("matlab/", views.matlab, name="matlab"),  # New URL for MATLAB course page
    path("solidworks/", views.solidworks, name="solidworks"),  # New
    path("all_courses/staddpro/", views.staad_pro, name="staddpro"),  # New URL for STAAD Pro course page

    
    # Add any other URLs as needed
    

]