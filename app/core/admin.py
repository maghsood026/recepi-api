from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext as _

from .models import User


class AdminUser(UserAdmin):
    ordering = ['id']
    list_display = ['id', 'email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(User, AdminUser)
