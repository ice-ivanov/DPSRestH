from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.utils.translation import ugettext_lazy as _

from accounts.forms import UserAdminCreationForm, UserAdminChangeForm
from accounts.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """
    User admin.
    """
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    change_password_form = AdminPasswordChangeForm
    fieldsets = (
        (_('Personal Info'), {'fields': ('phone', 'first_name', 'email', 'language')}),
        (_('Permissions'), {'fields': ('is_superuser', 'is_staff', 'groups')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'first_name', 'password1', 'password2'),
        }),
    )
    list_display = ('phone', 'first_name', 'is_active')
    list_filter = ('is_active', 'is_staff')
    search_fields = ('phone', 'name', 'email')
    readonly_fields = ('is_superuser',)
