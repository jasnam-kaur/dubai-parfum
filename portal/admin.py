from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Add 'role' and 'company_name' to the admin panels
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'company_name', 'phone_number')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role', 'company_name', 'phone_number')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)