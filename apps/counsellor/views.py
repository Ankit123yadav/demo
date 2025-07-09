from django.shortcuts import render

# Create your views here.
def add_student(request):
    return render(request, 'Counsellor_management/templates/Add_student.html')

def student_list(request):
    return render(request, 'Counsellor_management/templates/Student_list.html')


def batch(request):
    return render(request, 'Counsellor_management/templates/batch.html')

def course(request):
    return render(request, 'Counsellor_management/templates/course.html')

def student_feedback(request):
    return render(request, 'Counsellor_management/templates/student_feedback.html')