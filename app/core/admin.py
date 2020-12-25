from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class AdminUser(UserAdmin):
    ordering = ['id']
    list_display = ['id', 'email']


admin.site.register(User, AdminUser)
