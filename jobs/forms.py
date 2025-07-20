from django.forms import ModelForm
from django import forms
from .models import Job , Application

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description','company_name', 'role', 'industry', 'department',
                  'education', 'skills', 'location', 'job_type', 'sub_type','openings', 'min_salary_lpa',
                  'max_salary_lpa']
        widgets = {
            'job_type': forms.RadioSelect,
            'sub_type': forms.RadioSelect,
        }
        


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['content', 'experience' ]