from django.db import models

# Create your models here.
from utils.field_validators import national_code_validator, phone_regex
from utils.global_var import FIELD_CHOICES, LEVEL_CHOICES


class Student(models.Model):
    father_name=models.CharField(max_length=20,blank=True,null=True)
    father_phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True,null=True)
    field=models.CharField(max_length=7,choices=FIELD_CHOICES)
    level=models.CharField(max_length=2,choices=LEVEL_CHOICES)
    birth_certificate=models.ImageField(upload_to='student_birth_certificate',null=True,blank=True)
    profile=models.OneToOneField(to="user.Profile",on_delete=models.CASCADE,related_name="student")

    class Meta:
        verbose_name = "Student"



