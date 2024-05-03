from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import User, Key
from .forms import UserModelCreateForm, UserModelChangeForm


@admin.register(User)
class UserModelAdmin(ModelAdmin):
    add_form = UserModelCreateForm
    form = UserModelChangeForm
    list_display = ["username", "first_name", "last_name"]
    add_fieldssets = (
        ("Yangi foydalanuvchi qo'shish", {
            "fields": ("username", "first_name", "last_name", "jshshr", "phone", "password1", "password2", )
        }),
    )
    fieldsets = (
        ("Foydalanuvchini tahrirlash", {
            "fields": ("username", "first_name", "last_name", "jshshr", "phone", )
        }),
    )

@admin.register(Key)
class KeyModelAdmin(ModelAdmin):
    list_display = ["filename", "author"]
