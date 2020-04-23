from django.db import models


# Create your models here.


class Agent(models.Model):
    address = models.CharField(max_length=300,null=True,blank=True)
    profile = models.OneToOneField(to="user.Profile", on_delete=models.Case, related_name="agent")
    teacher = models.ManyToManyField(to="Agent", related_name="agent", null=True, blank=True)
    center = models.ForeignKey(to="center.Center", on_delete=models.CASCADE, related_name="agent")
    top_agent = models.ForeignKey(to="self", on_delete=models.CASCADE, related_name="subagent",null=True,blank=True)

    class Meta:
        verbose_name = 'Agent'
