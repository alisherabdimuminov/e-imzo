from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class UserModelCreateForm(UserCreationForm):
    class Meta:
        fields = ("username", "first_name", "last_name", "jshshr", "phone", "password1", "password2")

class UserModelChangeForm(UserChangeForm):
    class Meta:
        fields = ("username", "first_name", "last_name", "jshshr", "phone")
