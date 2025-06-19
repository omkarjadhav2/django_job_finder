from django.shortcuts import render, redirect
from django.contrib.auth import login ,authenticate , logout
from .forms import EmployerRegisterForm, SeekerRegisterForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render , HttpResponse
from django.contrib import messages
def home(request):
    context = {
        'user': 'omkar'
    }
    return render(request , 'registration/index.html' )

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

def user_login(request):
    if request.method =='POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('home')
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid login credentials'})
    return render(request, 'registration/login.html')
        
def user_logout(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            logout(request)
            print("function working")
            messages.success(request, 'Logout successful.')
    return redirect('login_user')