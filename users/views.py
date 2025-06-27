from django.shortcuts import render, redirect
from django.contrib.auth import login ,authenticate , logout 
from .forms import SeekerRegisterForm , SeekerProfileForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render , get_object_or_404
from django.contrib import messages
from jobs.models import Job
from .models import SeekerProfile 
def show_jobs(request):
    jobs = Job.objects.filter(is_approved = True)
    context = {
        'jobs': jobs
    }
    return render(request , 'users/index.html' , context )



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
            messages.success(request, 'Logout successful.')
    return redirect('login_user')


def job_card(request , slug):
    job = get_object_or_404(Job, slug=slug)
    print(job)
    return render(request, 'users/job_card.html' , {'job':job})



def profile(request):
    user_profile = get_object_or_404(SeekerProfile, user=request.user)
    return render(request, 'users/profile.html', {'user_profile': user_profile})



def edit_profile(request):
    user_profile = get_object_or_404(SeekerProfile, user=request.user)

    if request.method == 'POST':
        form = SeekerProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # adjust this if your url name is different
    else:
        form = SeekerProfileForm(instance=user_profile)

    return render(request, 'users/edit_profile.html', {'form': form})