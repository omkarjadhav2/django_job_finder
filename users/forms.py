from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, SeekerProfile , EmployerProfile , Experience


class SeekerRegisterForm(UserCreationForm):
   
    class Meta:
        model = CustomUser
        fields = ['first_name' , 'last_name','username', 'email', 'password1', 'password2'  ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_seeker = True
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            SeekerProfile.objects.create(
            user=user,
            first_name=user.first_name,
            last_name=user.last_name
        )
        return user


class EmployerRegisterForm(UserCreationForm):
    company_name = forms.CharField()

    class Meta:
        model = CustomUser
        fields = ['first_name' , 'last_name', 'username', 'email', 'password1', 'password2' , 'company_name']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_employer = True
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.company_name=self.cleaned_data['company_name']
        if commit:
            user.save()
            EmployerProfile.objects.create(user=user, 
            company_name=user.company_name ,
            first_name=user.first_name,
            last_name=user.last_name)
        return user


class SeekerProfileForm(forms.ModelForm):
    class Meta:
        model = SeekerProfile
        fields = [
            'first_name',
            'last_name',
            'contact',
            'resume',
        ]
    
class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['company_name', 'role', 'years']
