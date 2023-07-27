from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from contacts_list.models import Contacts, User


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "address", "created_at"]
    search_fields = ["name", "email", "phone", "address", "created_at"]
    list_filter = ["name", "email", "phone", "address", "created_at"]
    list_per_page = 10


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display
    search_fields = UserAdmin.list_display
    list_filter = UserAdmin.list_display
    list_per_page = 10