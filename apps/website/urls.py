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
    path("all_courses/python/", views.python, name="python"),  # New URL for Python course page
    path("demo/", views.demo, name="demo"),  # New URL for demo page
    path("download_certificate/", views.download_certificate, name="download_certificate"),  # New URL for downloading certificate
    path("all_courses/digital_marketing/", views.digital_marketing, name="digital_marketing"),  # New URL for Digital Marketing course page
    path("all_courses/android/", views.android, name="android"),  # New URL for Android course page 
    path("all_courses/mern/", views.mern, name="mern"),  # New URL for MERN course page
    path("all_courses/asp_net/", views.asp_net, name="asp_net"),  # New URL for ASP.NET course page
    path("all_courses/iot/", views.iot, name="iot"),  # New URL for IoT
    path("all_courses/autocad/", views.autocad, name="autocad"),  # New URL for AutoCAD course page
    path("all_courses/cybersecurity/", views.cybersecurity, name="cybersecurity"),  # New URL for Cyber Security course page
    path("all_courses/automation/", views.automation, name="automation"),  # New URL for Automation course page
    path("all_courses/pcb/", views.pcb, name="pcb"),  # New URL for PCB course page
    path("all_courses/plc/", views.plc, name="plc"),
    path("all_courses/data_science/", views.data_science, name="data_science"),  # New URL for Data Science course page
    path("all_courses/ecad/", views.ecad, name="ecad"),  # New URL for ECAD course page
    path("all_courses/3DMax/", views.D3max, name="3DMax"),  # New URL for 3DMax course page
    path("all_courses/plumbing/", views.plumbing, name="plumbing"),  # New URL for Plumbing course page
    path("all_courses/hvac/", views.hvac, name="hvac"),  # New URL for HVAC course page
    path("all_courses/embedded/", views.embedded, name="embedded"),  # New URL for Embedded Systems course page
    path("all_courses/matlab/", views.matlab, name="matlab"),  # New URL for MATLAB course page
    path("all_courses/solidworks/", views.solidworks, name="solidworks"),  # New
    path("all_courses/staddpro/", views.staad_pro, name="staddpro"),  # New URL for STAAD Pro course page

    path("all_courses/revit/", views.revit, name="revit"),  # New URL for Revit course page
    path("all_courses/php/", views.php, name="php"),  # New URL for PHP course page
    path("all_courses/java/", views.java, name="java"),
    path("all_courses/ai/", views.ai, name="ai"),  # New URL for AI course page
    path("all_courses/robotics/", views.robotics, name="robotics"),

    
    # Add any other URLs as needed
    

]