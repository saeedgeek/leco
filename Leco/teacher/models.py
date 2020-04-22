from django.db import models

# Create your models here.
from utils.field_validators import phone_regex


class Teacher(models.Model):
    secound_phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=False)
    profile = models.OneToOneField(to="user.Profile", on_delete=models.Case, related_name="teacher")
    lessons = models.ManyToManyField(to="class_room.Lesson", related_name="teacher")

    class Meta:
        verbose_name = 'Teacher'
