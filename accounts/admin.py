from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Профиль'
    fields = ['phone']


class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline]
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'phone_display']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    list_filter = ['is_staff', 'is_superuser', 'is_active']

    def phone_display(self, obj):
        return obj.profile.phone if hasattr(obj, 'profile') else ''

    phone_display.short_description = 'Телефон'


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)