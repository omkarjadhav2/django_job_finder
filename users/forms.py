from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, EmployerProfile, SeekerProfile

class EmployerRegisterForm(UserCreationForm):
    company_name = forms.CharField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_employer = True
        if commit:
            user.save()
            EmployerProfile.objects.create(user=user, company_name=self.cleaned_data['company_name'])
        return user

class SeekerRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_seeker = True
        if commit:
            user.save()
            SeekerProfile.objects.create(user=user)
        return user
