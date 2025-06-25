from django.db import models
from users.models import CustomUser
from django.utils.text import slugify


class Location(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('fulltime', 'Full-Time'),
        ('parttime' , 'Part-Time'),
        ('internship' , 'Internship'),
    ]
    employer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=250)
    industry = models.CharField(max_length=250)
    department = models.CharField(max_length=250)
    education = models.CharField(max_length=500)
    skills = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    min_salary_lpa = models.DecimalField(max_digits=5 , decimal_places=2 , null=True , blank=True)
    max_salary_lpa = models.DecimalField(max_digits=5 , decimal_places=2 , null=True , blank=True)
    job_type = models.CharField(max_length=20 , choices= JOB_TYPE_CHOICES , default='fulltime')
    company_name = models.CharField(max_length=250)
    

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


