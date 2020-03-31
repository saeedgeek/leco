from django.db import models

# Create your models here.
class Center(models.Model):
    profile = models.OneToOneField(to="user.Profile", on_delete=models.Case, related_name="center")
    class Meta:
        verbose_name = 'Center'