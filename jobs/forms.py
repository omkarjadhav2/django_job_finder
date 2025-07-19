from django.forms import ModelForm
from django import forms
from .models import Job , Application , Skill

class JobForm(ModelForm):
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'select2-multiple'}), # Or a custom widget for advanced tagging
        required=False # Allow jobs to be posted without skills initially
    )

    class Meta:
        model = Job
        fields = ['title', 'description','company_name', 'role', 'industry', 'department',
                  'education', 'skills', 'location', 'min_salary_lpa',
                  'max_salary_lpa', 'job_type']
        


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['content', 'experience' ]