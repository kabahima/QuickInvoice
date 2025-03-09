from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Define a custom UserAdmin to display additional fields in the admin interface
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'first_name', 'last_name', 'role', 'phone_number', 'address', 'is_staff']
    list_filter = ['role', 'is_staff', 'is_superuser']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering = ['username']

    # Add fields to the "add user" and "change user" forms
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'phone_number', 'address')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'phone_number', 'address')}),
    )

# Register the custom user admin
admin.site.register(User, CustomUserAdmin)
