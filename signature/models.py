from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import UserManager
from .utils import generate_key, generate_filename


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    jshshr = models.CharField(max_length=100, unique=True)
    phone = models.CharField(max_length=20)

    objects = UserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return self.username
    
class Key(models.Model):
    token = models.CharField(max_length=200, default=generate_key)
    filename = models.CharField(max_length=200, default=generate_filename)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.token
