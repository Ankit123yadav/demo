from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "website/index.html")

def about(request):
    return render(request, "website/About.html")

def registration(request):
    return render(request, "website/Registration.html")

def apprenticeship(request):
    return render(request, "website/Apprenticeship.html")

def carrer(request):
    return render(request, "website/Carrer.html")

def contactus(request):
    return render(request, "website/Contactus.html")

def courses(request):
    return render(request, "website/Course.html")

def ceme(request):
    return render(request, "website/CEME.html")

def digital(request):
    return render(request, "website/digital.html")

def csit(request):
    return render(request, "website/csit.html")

def eeec(request):
    return render(request, "website/EEEC.html")

def expert(request):
    return render(request, "website/Expert.html")

def industrials(request):
    return render(request, "website/Industrial.html")

def semgallery(request):
    return render(request, "website/semgallery.html")

def software(request):
    return render(request, "website/software.html")

def mobile(request):
    return render(request, "website/mobile.html")

def website(request):
    return render(request, "website/website.html")

def winter(request):
    return render(request, "website/winter.html")

def teamgallery(request):
    return render(request, "website/teamgallery.html")

def verified(request):
    return render(request, "website/verified.html")   

def syllabus(request):
    return render(request, "website/syllabus.html")

def demo(request):
    return render(request, "website/demo.html")    

def download_certificate(request):
    return render(request, "website/download_certificate.html")