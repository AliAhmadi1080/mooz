from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib import admin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = UserAdmin.list_display
    fieldsets = UserAdmin.fieldsets
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('student info',{"fields": ('first_name','last_name'),},),
        )

admin.site.register(CustomUser, CustomUserAdmin)