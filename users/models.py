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

class Location(models.Model):
    seeker = models.OneToOneField(SeekerProfile, on_delete=models.CASCADE, related_name='location')
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.city}, {self.state}, {self.country}"

class Education(models.Model):
    seeker = models.ForeignKey(SeekerProfile, on_delete=models.CASCADE, related_name='educations')
    field = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    year_completed = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.level} in {self.field} from {self.institution}"

class Experience(models.Model):
    seeker = models.ForeignKey(SeekerProfile, on_delete=models.CASCADE, related_name='experiences')
    company_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255, blank=True)
    duration = models.CharField(max_length=20)  # e.g. "2 years", "6 months"
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.role} at {self.company_name}"
