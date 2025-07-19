from django.contrib import admin
from .models import Job , Location ,Application


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['employer', 'title', 'is_approved', 'created_at']
    list_filter = ['is_approved', 'created_at']
    search_fields = ['title', 'description', 'role', 'employer__email']
    ordering = ['-created_at']
    
admin.site.register(Location)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'job', 'applied_at')
    readonly_fields = ('applied_at',)
    fields = ('applicant', 'job', 'content', 'experience', 'applied_at')