from django.shortcuts import render

# Create your views here.
def add_trainer(request):
    return render(request, 'Trainer/add_trainer.html')

def trainer_list(request):
    return render(request, 'Trainer/trainer_list.html')

def trainer_schedule(request):
    return render(request, 'Trainer/trainer_schedule.html')

def feedback(request):
    return render(request, 'Trainer/feedback.html')