from django.shortcuts import render,redirect
from .models import Registration
from django.contrib import messages
# Create your views here.




def student_register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful!")
            return redirect('student_register')  # Redirect to same page or success page
    else:
        form = Registration()

    return render(request, 'website/registration.html', {'form': form})
