from django.shortcuts import render, redirect
from django.contrib import messages
from apps.form.models import Registration, WorkshopRegistration

# Create your views here.
def index(request):
    return render(request, "website/index.html")

def about(request):
    return render(request, "website/About.html")

def registration(request):
    if request.method == 'POST':
        form_kind = request.POST.get('form_kind')
        try:
            if form_kind == 'student':
                Registration.objects.create(
                    full_name=request.POST.get('full_name', '').strip(),
                    phone=request.POST.get('phone', '').strip(),
                    guardian_number=request.POST.get('guardian_number', '').strip(),
                    email=request.POST.get('email', '').strip(),
                    father_name=request.POST.get('father_name', '').strip(),
                    mother_name=request.POST.get('mother_name', '').strip(),
                    gender=request.POST.get('gender', '').strip(),
                    dob=request.POST.get('dob'),
                    address=request.POST.get('address', '').strip(),
                    qualification=request.POST.get('qualification', '').strip(),
                    branch=request.POST.get('branch', '').strip(),
                    year=request.POST.get('year', '').strip(),
                    semester=request.POST.get('semester', '').strip(),
                    college_name=request.POST.get('college_name', '').strip(),
                    percentage_or_cgpa=request.POST.get('percentage_or_cgpa', '').strip() or None,
                    course_name=request.POST.get('course_name', '').strip(),
                    duration=request.POST.get('duration', '').strip(),
                    mode=request.POST.get('mode', '').strip(),
                )
            elif form_kind == 'workshop':
                WorkshopRegistration.objects.create(
                    full_name=request.POST.get('full_name', '').strip(),
                    phone=request.POST.get('phone', '').strip(),
                    email=request.POST.get('email', '').strip(),
                    workshop_name=request.POST.get('course_name', '').strip(),
                )
            else:
                messages.error(request, 'Invalid form submission.')
                return redirect('registration')

            messages.success(request, 'Registration submitted successfully!')
            return redirect('/dashboard/all_users/')
        except Exception:
            messages.error(request, 'There was a problem saving your registration. Please try again.')
            return redirect('registration')

    return render(request, "form/Registration.html")

def apprenticeship(request):
    return render(request, "website/Apprenticeship.html")

def carrer(request):
    return render(request, "website/Carrer.html")

def contactus(request):
    return render(request, "form/Contactus.html")

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

def eventgallery(request):
    return render(request, "website/eventgallery.html")

def verified(request):
    return render(request, "website/verified.html")   

def syllabus(request):
    return render(request, "website/syllabus.html")

def demo(request):
    return render(request, "website/demo.html")    

def download_certificate(request):
    return render(request, "website/download_certificate.html")

def all_courses(request):
    return render(request, "website/All_courses.html")

def python(request):
    return render(request, "website/all_courses/python.html")

def digital_marketing(request):
    return render(request, "website/all_courses/digital _marketing.html")    

def android(request):
    return render(request, "website/all_courses/android.html")    

def mern(request):
    return render(request, "website/all_courses/mern_stack.html")    

def asp_net(request):
    return render(request, "website/all_courses/asp net.html")

def iot(request):
    return render(request, "website/all_courses/IOT.html")      


def autocad(request):       
    return render(request, "website/all_courses/autocad.html")   

def cybersecurity(request):
    return render(request, "website/all_courses/cybersecurity.html")

def pcb(request):
    return render(request, "website/all_courses/pcb.html")


def plc(request):
    return render(request, "website/all_courses/plc.html")

def automation(request):
    return render(request, "website/all_courses/automation.html")    

def D3max(request):
    return render(request, "website/all_courses/3DMax.html")   


def data_science(request):
    return render(request, "website/all_courses/data_science.html")

def ecad(request):
    return render(request, "website/all_courses/ecad.html")


def embedded(request):
    return render(request, "website/all_courses/embedded.html")


def hvac(request):
    return render(request, "website/all_courses/hvac.html")



def matlab(request):
    return render(request, "website/all_courses/Matlab.html")


def plumbing(request):
    return render(request, "website/all_courses/plumbing.html")

def solidworks(request):
    return render(request, "website/all_courses/solidworks.html")

def staad_pro(request):
    return render(request, "website/all_courses/staad_pro.html")        

def revit(request):
    return render(request, "website/all_courses/Revit_Architect.html")

def robotics(request):
    return render(request, "website/all_courses/robotics.html")
  

def java(request):
    return render(request, "website/all_courses/javaa.html")

def php(request):
    return render(request, "website/all_courses/php.html")


def ai(request):
    return render(request, "website/all_courses/ai.html")


def data_analytics(request):
    return render(request, "website/all_courses/data_analytics.html")


def delhi_ncr(request):
    return render(request, "website/dem.html")
    
def adobe_photoshop(request):
    return render(request, "website/all_courses/adobe_photoshop.html")


def aadobe_illustrator(request):
    return render(request, "website/all_courses/adobe_illustrator.html")


def adobe_xd(request):
    return render(request, "website/all_courses/adobe_xd.html")



def workshop_registration(request):
    return render(request, "form/workshop_registration.html")
        