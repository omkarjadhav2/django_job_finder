from django.forms import ModelForm
from .models import Job , Application

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description','company_name', 'role', 'industry', 'department',
                  'education', 'skills', 'location', 'min_salary_lpa',
                  'max_salary_lpa', 'job_type']


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['content', 'experience' ]