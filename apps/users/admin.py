from django.contrib import admin
from apps.users.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'is_paid','is_verified', 'role', 'date_joined']
    search_fields = ['email', 'first_name', 'last_name']
    list_filter = ['is_active', 'is_superuser', 'is_paid', 'role', 'is_verified']
    ordering = ['email']

admin.site.register(User, UserAdmin)
