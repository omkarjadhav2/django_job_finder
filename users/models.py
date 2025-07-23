from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.text import slugify


class CustomUser(AbstractUser):
    is_employer = models.BooleanField(default=False)
    is_seeker = models.BooleanField(default=False)


class SeekerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    contact = models.CharField(max_length=15, blank=True)
    resume = models.FileField(null=True , blank=True , upload_to="resume/")

    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(f"{self.first_name} {self.last_name}")
            slug = base_slug
            counter = 1
            while SeekerProfile.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class EmployerProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Experience(models.Model):
    seeker = models.ForeignKey(SeekerProfile, on_delete=models.CASCADE, related_name="experiences")
    company_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    years = models.DecimalField(max_digits=4, decimal_places=1)  

    def __str__(self):
        return f"{self.role} at {self.company_name}"
    
class Education(models.Model):
    seeker = models.ForeignKey(SeekerProfile, on_delete=models.CASCADE, related_name="educations")
    institute_name = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)
    passing_year = models.IntegerField()

    def __str__(self):
        return f"{self.course_name} in {self.institute_name}"
    
    
    