from django.shortcuts import render, redirect
from django.contrib.auth import login ,authenticate , logout 
from .forms import SeekerRegisterForm , SeekerProfileForm , EmployerRegisterForm , ExperienceForm , EducationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render , get_object_or_404
from django.contrib import messages
from jobs.models import Job , Application
from .models import SeekerProfile  , Experience , Education , EmployerProfile
from jobs.forms import ApplicationForm
from django.utils import timezone
from .decorators import employer_required
from django.views.generic import  ListView
from django.db.models import Q
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from django.forms import modelformset_factory


def show_jobs(request):
    jobs = Job.objects.filter(is_approved=True).order_by('-created_at')
    paginator = Paginator(jobs, 3)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    
    context = {
        'jobs': jobs,
        'page_obj': page_obj
    }
    return render(request , 'users/index.html' , context )

class SearchResultsView(ListView):
    model = Job
    template_name = 'users/search_results.html'
    paginate_by = 5
    def get_queryset(self):
        query = self.request.GET.get("q") 
        location = self.request.GET.get("L")
        job_list = Job.objects.all() 
        if query:
            job_list = job_list.filter(
                Q(title__icontains=query) | Q(skills__icontains=query) | Q(description__icontains=query)
            )
        if location:
            job_list = job_list.filter(location__name__icontains=location)
        return job_list


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
    return render (request , 'users/apply_job.html' , {'form': form , "job": job})



def profile(request):
    user = request.user

    if user.is_authenticated:
        if user.is_seeker:
            profile = get_object_or_404(SeekerProfile, user=request.user)
        elif user.is_employer:
            profile = get_object_or_404(EmployerProfile, user=user)
    return render(request, 'users/profile.html', {'user_profile': profile})



def edit_profile(request):
    user_profile = get_object_or_404(SeekerProfile, user=request.user)

    ExperienceFormSet = modelformset_factory(Experience, form=ExperienceForm, extra=1, can_delete=True)
    EducationFormSet = modelformset_factory(Education, form=EducationForm, extra=1, can_delete=True)
    experience_qs = Experience.objects.filter(seeker=user_profile)
    education_qs = Education.objects.filter(seeker=user_profile)

    if request.method == 'POST':
        form = SeekerProfileForm(request.POST, request.FILES, instance=user_profile)
        formset = ExperienceFormSet(request.POST, queryset=experience_qs)
        education_formset = EducationFormSet(request.POST, queryset=education_qs)

        if form.is_valid() and formset.is_valid() and education_formset.is_valid():
            form.save()
            experiences = formset.save(commit=False)
            educations = education_formset.save(commit=False)

            for exp in experiences:
                exp.seeker = user_profile
                exp.save()
                
            for edu in educations:
                edu.seeker = user_profile
                edu.save()

            for obj in formset.deleted_objects:
                obj.delete()
            
            for obj in education_formset.deleted_objects:
                obj.delete()

            return redirect('profile')
    else:
        form = SeekerProfileForm(instance=user_profile)
        formset = ExperienceFormSet(queryset=experience_qs)
        education_formset = EducationFormSet(queryset=education_qs)

    context = {
        'form': form,
        'formset': formset,
        'education_formset': education_formset
    }

    return render(request, 'users/edit_profile.html', context)

@login_required
def seeker_dashboard(request):
    applications = Application.objects.filter(applicant=request.user).order_by('-applied_at')
    return render(request, 'users/seeker_dashboard.html', {'applications': applications})


