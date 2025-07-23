from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, SeekerProfile ,EmployerProfile , Experience

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_employer', 'is_seeker', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('User Type', {'fields': ('is_employer', 'is_seeker')}),
    )

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1
    
@admin.register(SeekerProfile)
class SeekerProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'contact']
    inlines = [ExperienceInline]

admin.site.register(EmployerProfile)

