from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, SeekerProfile ,EmployerProfile

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_employer', 'is_seeker', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('User Type', {'fields': ('is_employer', 'is_seeker')}),
    )


@admin.register(SeekerProfile)
class SeekerProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'contact']

admin.site.register(EmployerProfile)