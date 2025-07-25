from django.shortcuts import render, redirect ,get_object_or_404
from .models import Job , Application
from django.contrib.auth.decorators import login_required
from users.decorators import employer_required
from django.contrib import messages
from jobs.forms import JobForm , ApplicationForm


@login_required
@employer_required
def post_job(request):
    
    if request.method == "POST":
        form = JobForm(request.POST , request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.employer = request.user  
            job.save()
            return redirect('employer_dashboard')  
    else:
        form = JobForm()
    return render(request, 'jobs/post_job.html', {'form': form })

def create(request):
    try:
        if request.method == 'POST':
             form = JobForm(request.POST , request.FILES)
             job = form.save(commit=False)
             job.employer = request.user  
             job.save()
             return redirect('employer_dashboard')
        else:
            print(form.errors)
    except Exception as e:
        import traceback
    print(traceback.format_exc())


@login_required
@employer_required
def employer_dashboard(request):
    jobs = Job.objects.filter(employer=request.user)
    return render(request, 'jobs/dashboard.html', {'jobs': jobs})

@login_required
@employer_required
def update_post(request, slug):
    job = get_object_or_404(Job, employer=request.user, slug=slug )

    if request.method == 'POST':
        form = JobForm(request.POST , request.FILES, instance=job)
        if form.is_valid():
            form.save()
        messages.success(request, 'Post updated successfully.')
        return redirect('employer_dashboard')
    else:
        form = JobForm(instance=job)
    context = {
        'form': form,
    }
    return render(request, 'jobs/update_job.html', context)

@login_required
@employer_required
def delete_post(request, slug):
    job = get_object_or_404(Job, employer=request.user, slug=slug)

    if request.method == 'POST':
        job.delete()

        messages.success(request, 'Post deleted successfully.')
        return redirect('employer_dashboard')

    return render(request, 'jobs/delete_job.html', {'job': job})

@login_required
@employer_required
def view_applications(request , slug):
    applications = Application.objects.filter(job__employer = request.user ,job__slug = slug )
    return render(request, 'jobs/job_applications.html', {'applications': applications})
