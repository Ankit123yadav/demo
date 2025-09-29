from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Registration

# from apps.student_management.models import Registration
from apps.form.models import Registration

@login_required
def add_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        profile_file = request.FILES.get('profile_file')

        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Handle file upload if present
        if profile_file:
            fs = FileSystemStorage()
            filename = fs.save(profile_file.name, profile_file)
            # Optionally, associate the file with the user profile here

        messages.success(request, 'User added successfully!')
        return redirect('add_user')
    return render(request, 'student_management/templates/add_new_user.html')




# 1. Save data from form
def register_user(request):
    if request.method == 'POST':
        Registration.objects.create(
            full_name = request.POST['full_name'],
            phone = request.POST['phone'],
            email = request.POST['email'],
            father_name = request.POST['father_name'],
            address = request.POST['address'],
            qualification = request.POST['qualification'],
            branch = request.POST['branch'],
            college_name = request.POST['college_name'],
            course_name = request.POST['course_name'],
         
        )
        return redirect('all_users')  # after saving, show all users

    return render(request, 'student_management/templates/registration.html')  # form page

# 2. Show all submitted users
def all_users(request):
    users = Registration.objects.all().order_by('-email')
    return render(request, 'student_management/templates/all_user.html', { 'users': users })

def workshop_student(request):
    # users = Registration.objects.all().order_by('-email')
    return render(request, 'student_management/templates/workshop_student.html')

# def all_users(request):
#     users = Registration.objects.all()
    
#     # return render(request, 'student_management/templates/all_users.html', {'users': users})
#     return render(request, 'student_management/templates/all_user.html',{ 'users': users})

