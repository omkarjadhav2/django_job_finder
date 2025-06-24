from django.forms import ModelForm
from .models import Job

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'role', 'industry', 'department',
                  'education', 'skills', 'location', 'min_salary_lpa',
                  'max_salary_lpa', 'job_type']
