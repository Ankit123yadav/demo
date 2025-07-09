from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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
    return render(request, 'usermangement/templates/add_new_user.html')
