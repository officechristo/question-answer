from .forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('name', 'email', 'is_active')
    list_filter = ('name', 'email', 'is_active')
    fieldsets = (
        (None, {'fields': ('name', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')})
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, UserAdmin)
