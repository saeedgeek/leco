from django.db import models
from uuid import uuid4
# Create your models here.
class ClassRoom(models.Model):
    name=models.CharField(max_length=20)
    code=uuid4()
    fee=models.PositiveSmallIntegerField()
    semester=models.CharField(max_length=4)
    lesson=models.ForeignKey(to="Lesson",on_delete=models.CASCADE)
    content=models.ManyToManyField(to="Content",related_name="class_room",through="ClassContent")
    student=models.ManyToManyField(to="student.Student",related_name="class_room",through="StudentClass")
    agent=models.ForeignKey(to="agent.Agent",on_delete=models.CASCADE,related_name="class_room")
    teacher=models.ForeignKey(to="teacher.Teacher",on_delete=models.CASCADE,related_name="class_room")


class StudentClass(models.Model):
    student=models.ForeignKey(to="student.Student",on_delete=models.CASCADE)
    class_room=models.ForeignKey(to=ClassRoom,on_delete=models.CASCADE)
    is_register=models.BooleanField(default=False)
    grade=models.PositiveSmallIntegerField(default=101)



class ClassContent(models.Model):
    content=models.ForeignKey(to="Content",on_delete=models.CASCADE)
    class_room=models.ForeignKey(to="ClassRoom",on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)


class Lesson(models.Model):
    name = models.CharField(max_length=20)
    pre_required=models.ForeignKey(to="self",null=True,blank=True,related_name="post_reuired",on_delete=models.CASCADE)



class Present_Absent(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    class_room=models.ForeignKey(to=ClassRoom,on_delete=models.CASCADE)
    student=models.ForeignKey(to="student.Student",on_delete=models.CASCADE)
    class Meta:
        unique_together=(("date","student","class_room"),)




class Content(models.Model):
    name=models.CharField(max_length=20)
    text=models.CharField(max_length=500)
    media=models.FileField(upload_to="file")
    time=models.TimeField(auto_now_add=True)
