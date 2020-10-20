from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

    
class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    username = models.CharField(max_length=30, unique=False)
    phone = models.CharField(max_length=1000, unique=True)
    is_staff = models.BooleanField(_('staff status'),default=False)
    is_active = models.BooleanField(_('active'), default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def str_username(username: str) ->str:
        return username

    def phone_no (phone: int) ->int:
        if phone<1000:
            return None
        if phone == 0:
            return 1
        return phone