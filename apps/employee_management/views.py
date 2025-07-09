from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Department, Designation




def employee_list(request):
    return render(request, 'employee_management/templates/employee_list.html')

@login_required
def add_employee(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        profile_file = request.FILES.get('profile_file')

        # Create user (employee)
        user = user.objects.create_user(username=username, email=email, password=password)
        if full_name:
            names = full_name.split(' ', 1)
            user.first_name = names[0]
            if len(names) > 1:
                user.last_name = names[1]
        user.save()

        # Handle file upload if present
        if profile_file:
            fs = FileSystemStorage()
            filename = fs.save(profile_file.name, profile_file)
            # Optionally, associate the file with the user profile here

    #     messages.success(request, 'Employee added successfully!')
        return redirect('employee_list')
    return render(request, 'employee_management/templates/add_employee.html')


def designation(request):
    return render(request, 'employee_management/templates/designation.html')

def department_list(request):
    departments = Department.objects.all()
    return render(request, 'employee_management/templates/department_list.html', {'departments': departments})

def add_department(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        if name:
            Department.objects.create(name=name, description=description)
            return redirect('department_list')
    return render(request, 'employee_management/templates/add_department.html')

def designation_list(request):
    designations = Designation.objects.all()
    return render(request, 'employee_management/designation_list.html', {'designations': designations})

def add_designation(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        if name:
            Designation.objects.create(name=name, description=description)
            return redirect('designation_list')
    return render(request, 'employee_management/add_designation.html')

def add_dummy_designations(request):
    # Utility view for adding dummy designations (for testing/demo)
    Designation.objects.get_or_create(name='Manager', defaults={'description': 'Manages team'})
    Designation.objects.get_or_create(name='Developer', defaults={'description': 'Develops software'})
    Designation.objects.get_or_create(name='Designer', defaults={'description': 'Designs UI/UX'})
    return redirect('designation_list')

def attendance(request):
    # Placeholder for attendance management view
    return render(request, 'employee_management/templates/attendance.html')

def leave_request(request):
    # Placeholder for leave request management view
    return render(request, 'employee_management/templates/leave_request.html')

def payroll(request):
    # Placeholder for payroll management view
    return render(request, 'employee_management/templates/payroll.html')

def holidays(request):
    # Placeholder for holidays management view
    return render(request, 'employee_management/templates/holidays.html')

def performance_review(request):
    # Placeholder for performance review management view
    return render(request, 'employee_management/templates/performance_review.html')
