from django.shortcuts import render , HttpResponse


def members(request):
    context = {
        'myname':'omkar'
    }
    return render(request , 'registration/index.html' , context)

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import EmployerRegisterForm, SeekerRegisterForm

def register_employer(request):
    if request.method == 'POST':
        form = EmployerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('employer_dashboard')
    else:
        form = EmployerRegisterForm()
    return render(request, 'registration/register_employer.html', {'form': form})

def register_seeker(request):
    if request.method == 'POST':
        form = SeekerRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SeekerRegisterForm()
    return render(request, 'registration/register_seeker.html', {'form': form})
