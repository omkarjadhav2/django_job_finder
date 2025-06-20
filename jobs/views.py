from django.shortcuts import render, redirect ,get_object_or_404
from .models import Job
from django.contrib.auth.decorators import login_required
from users.decorators import employer_required
from django.contrib import messages

@login_required
@employer_required
def post_job(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Job.objects.create(employer=request.user, title=title, description=description)
        return redirect('employer_dashboard')
    return render(request, 'jobs/post_job.html')

@login_required
@employer_required
def employer_dashboard(request):
    jobs = Job.objects.filter(employer=request.user)
    return render(request, 'jobs/dashboard.html', {'jobs': jobs})

@login_required
@employer_required
def update_post(request, id):
    job = get_object_or_404(Job, employer=request.user, id=id)

    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        
        job.title = title
        job.description = description
        job.save()

        messages.success(request, 'Post updated successfully.')
        return redirect('employer_dashboard')

    return render(request, 'jobs/update_job.html', {'job': job})

@login_required
@employer_required
def delete_post(request, id):
    job = get_object_or_404(Job, employer=request.user, id=id)

    if request.method == 'POST':
        job.delete()

        messages.success(request, 'Post deleted successfully.')
        return redirect('employer_dashboard')

    return render(request, 'jobs/delete_job.html', {'job': job})