from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'email', 'chat_id', 'first_name', 'last_name', 'is_active')
    list_display_links = ('email', 'last_name', 'is_active')