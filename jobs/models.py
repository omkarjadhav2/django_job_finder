from django.db import models
from users.models import CustomUser
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field 

class Location(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full-time', 'Full-Time'),
        ('Part-time' , 'Part-Time'),
        ('Internship' , 'Internship'),
    ]
    JOB_SUB_TYPE_CHOICES = [
        ('In-Office', 'In-Office'),
        ('Remote' , 'Remote'),
        ('Hybrid' , 'Hybrid'),
    ]
    employer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, unique=True)
    description = CKEditor5Field('Job Description', config_name='default')
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=250)
    industry = models.CharField(max_length=250)
    department = models.CharField(max_length=250)
    education = models.CharField(max_length=500)
    skills = models.CharField(max_length=250)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    min_salary_lpa = models.DecimalField(max_digits=5 , decimal_places=2 , null=True , blank=True)
    max_salary_lpa = models.DecimalField(max_digits=5 , decimal_places=2 , null=True , blank=True)
    job_type = models.CharField(max_length=20 , choices= JOB_TYPE_CHOICES , default='Full-Time')
    sub_type = models.CharField(max_length=20 , choices= JOB_SUB_TYPE_CHOICES , default='In-Office')
    openings = models.IntegerField(null=True , blank=True)
    company_name = models.CharField(max_length=250)
    min_experience = models.IntegerField(null=True , blank=True)
    max_experience = models.IntegerField(null=True , blank=True)
    

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while Job.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class Application(models.Model):
    applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applied_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.applicant.username} -> {self.job.title}"
