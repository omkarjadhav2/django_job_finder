from django.db import models
from users.models import CustomUser

class Job(models.Model):
    employer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
