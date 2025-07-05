from django.shortcuts import render, redirect
from django.contrib.auth import login ,authenticate , logout 
from .forms import SeekerRegisterForm , SeekerProfileForm , EmployerRegisterForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render , get_object_or_404
from django.contrib import messages
from jobs.models import Job , Application
from .models import SeekerProfile 
from jobs.forms import ApplicationForm
from django.utils import timezone
from .decorators import employer_required
from django.views.generic import  ListView
from django.db.models import Q


def show_jobs(request):
    jobs = Job.objects.filter(is_approved=True).order_by('-created_at')
    
    context = {
        'jobs': jobs
    }
    return render(request , 'users/index.html' , context )

class SearchResultsView(ListView):
    model = Job
    template_name = 'users/search_results.html'
    def get_queryset(self):
        query = self.request.GET.get("q") 
        object_list =  Job.objects.filter(
            Q(title__icontains=query) | Q(skills__icontains=query)
        )
        return object_list


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
    return render(request, 'users/job_card.html' , {'job':job})

@login_required
def apply_for_job(request, slug):
    job = get_object_or_404(Job, slug=slug)
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.applied_at = timezone.now()
            application.save()
            messages.success(request, "applied succesfully")
            return redirect('home')
    else:
        form = ApplicationForm()
    return render (request , 'users/apply_job.html' , {'form': form})



def profile(request):
    user_profile = get_object_or_404(SeekerProfile, user=request.user)
    return render(request, 'users/profile.html', {'user_profile': user_profile})



def edit_profile(request):
    user_profile = get_object_or_404(SeekerProfile, user=request.user)

    if request.method == 'POST':
        form = SeekerProfileForm(request.POST ,request.FILES, instance=user_profile  )
        if form.is_valid():
            form.save()
            return redirect('profile') 
    else:
        form = SeekerProfileForm(instance=user_profile)

    return render(request, 'users/edit_profile.html', {'form': form})

@login_required
def seeker_dashboard(request):
    applications = Application.objects.filter(applicant=request.user)
    return render(request, 'users/seeker_dashboard.html', {'applications': applications})

@login_required
def application_status(request, id):
    application = get_object_or_404(Application, pk = id ,applicant = request.user)
    return render(request, 'users/application_status.html', {'application': application})

