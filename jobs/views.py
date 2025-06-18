from django.shortcuts import render , HttpResponse


def Showjobs(request):
    context = {
        'myname':'omkar'
    }
    return HttpResponse("jobs page")

from django.shortcuts import render, redirect
from .models import Job
from django.contrib.auth.decorators import login_required
from users.decorators import employer_required

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
