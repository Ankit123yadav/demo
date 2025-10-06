from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Registration, WorkshopRegistration

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

# Edit user
def edit_user(request, user_id):
    user = Registration.objects.get(id=user_id)
    if request.method == 'POST':
        user.full_name = request.POST.get('full_name')
        user.phone = request.POST.get('phone')
        user.email = request.POST.get('email')
        user.father_name = request.POST.get('father_name')
        user.address = request.POST.get('address')
        user.college_name = request.POST.get('college_name')
        user.qualification = request.POST.get('qualification')
        user.course_name = request.POST.get('course_name')
        user.save()
        return redirect('all_users')
    return render(request, 'student_management/templates/edit_user.html', {'user': user})

# Delete user
def delete_user(request, user_id):
    user = Registration.objects.get(id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('all_users')
    return render(request, 'student_management/templates/delete_user_confirm.html', {'user': user})

def workshop_student(request):
    if request.method == 'POST':
        WorkshopRegistration.objects.create(
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            father_name=request.POST.get('father_name'),
            address=request.POST.get('address'),
            college_name=request.POST.get('college_name'),
            qualification=request.POST.get('qualification'),
            branch=request.POST.get('branch'),
            workshop_name=request.POST.get('workshop_name'),
        )
        return redirect('workshop_student')
    users = WorkshopRegistration.objects.all().order_by('-registration_date')
    return render(request, 'student_management/templates/workshop_student.html', {'users': users})

# def all_users(request):
#     users = Registration.objects.all()
    
#     # return render(request, 'student_management/templates/all_users.html', {'users': users})
#     return render(request, 'student_management/templates/all_user.html',{ 'users': users})

