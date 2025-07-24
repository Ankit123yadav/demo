from django.shortcuts import render

# Create your views here.
def certifiicate(request):
    return render(request, "management/certificate.html")