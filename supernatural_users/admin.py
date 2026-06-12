from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import UserProfile

# Register your models here.

# Define an inline admin descriptor for UserProfile model
# This lets you edit the profile right inside the User page
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Supernatural Profile'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    
# Re-register UserAdmin to include our inline supernatural data
admin.site.unregister(User)
admin.site.register(User, UserAdmin)