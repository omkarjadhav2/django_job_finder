from django.shortcuts import render
from .forms import EmployerRegisterForm
from django.contrib.auth import login ,authenticate , logout 
from django.shortcuts import render, redirect


# Create your views here.
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