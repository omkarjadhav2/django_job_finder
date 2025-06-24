from django.contrib import admin
from .models import Job , Location
from .forms import JobForm


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['employer', 'title', 'is_approved', 'created_at']
    list_filter = ['is_approved', 'created_at']
    search_fields = ['title', 'description', 'role', 'employer__email']
    ordering = ['-created_at']
    
admin.site.register(Location)
