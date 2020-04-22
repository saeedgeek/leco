from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.field_validators import phone_regex, national_code_validator, password_regex
from utils.global_var import CITY_CHOICES, USER_TYPE_CHOICES


class Profile(AbstractUser):
    # first name
    # last name
    password = models.CharField(validators=[password_regex], max_length=128)
    username = models.CharField(max_length=10, validators=[national_code_validator, ], unique=True, primary_key=True)
    image = models.ImageField(upload_to='student_profile', null=True, blank=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=False, unique=True)
    user_type = models.CharField(choices=USER_TYPE_CHOICES, max_length=7)
    city = models.CharField(max_length=15, choices=CITY_CHOICES)

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'Profile'
