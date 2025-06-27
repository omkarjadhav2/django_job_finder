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

    skills = models.TextField(blank=True, help_text="Comma-separated skills, e.g. Python, JavaScript")
    education_field = models.CharField(max_length=255, blank=True)
    education_level = models.CharField(max_length=255, blank=True)
    experience_company = models.CharField(max_length=255, blank=True)
    company_duration = models.CharField(max_length=2, blank=True)

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