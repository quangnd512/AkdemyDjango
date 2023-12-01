from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User      

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'id')

# Register the custom UserAdmin for the default User model
admin.site.unregister(User)  # Unregister the default UserAdmin
admin.site.register(User, CustomUserAdmin)  # Register your custom UserAdmin
