from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student
from .forms import StudentRegistrationForm


def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student registered successfully!')
            return redirect('success')
    else:
        form = StudentRegistrationForm()
    
    context = {
        'form': form,
        'title': 'Student Registration Form'
    }
    return render(request, 'register.html', context)


def success(request):
    return render(request, 'success.html')


def student_list(request):
    students = Student.objects.all()
    context = {
        'students': students,
        'title': 'Registered Students'
    }
    return render(request, 'student_list.html', context)
