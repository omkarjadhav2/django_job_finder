from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, SeekerProfile 
from django_select2.forms import ModelSelect2MultipleWidget



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


class SeekerProfileForm(forms.ModelForm):
    class Meta:
        model = SeekerProfile
        fields = [
            'first_name',
            'last_name',
            'contact',
            'skills',
        ]
    