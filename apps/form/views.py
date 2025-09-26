from django.shortcuts import render,redirect
from .models import Registration,Contactus
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



# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')

#         # Save the contact form data to the database
#         contact_entry = Contactus(name=name, email=email, message=message)
#         contact_entry.save()

#         messages.success(request, "Your message has been sent successfully!")
#         return redirect('contact')  # Redirect to the same page or a success page

#     return render(request, 'templates/form/contactus.html')



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')

        contact_entry = Contactus(
            name=name,
            email=email,
            message=message,
            phone=phone,
            subject=subject
        )
        contact_entry.save()

        messages.success(request, "Your message has been sent successfully!")
        return redirect('contact')

    return render(request, 'templates/form/contactus.html')
