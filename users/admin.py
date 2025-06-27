from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, SeekerProfile , Location , Education , Experience

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_employer', 'is_seeker', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('User Type', {'fields': ('is_employer', 'is_seeker')}),
    )

class LocationInline(admin.StackedInline):
    model = Location
    can_delete = False
    extra = 0  # no extra blank forms

class EducationInline(admin.StackedInline):
    model = Education
    extra = 1  # allow adding more education entries

class ExperienceInline(admin.StackedInline):
    model = Experience
    extra = 1  # allow adding more experience entries

@admin.register(SeekerProfile)
class SeekerProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'contact']
    inlines = [LocationInline, EducationInline, ExperienceInline]

admin.site.register(Location)
admin.site.register(Education)
admin.site.register(Experience)