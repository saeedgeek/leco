# Generated by Django 3.0.4 on 2020-03-31 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0001_initial'),
        ('class_room', '0002_auto_20200331_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_room', to='teacher.Teacher'),
        ),
        migrations.AddField(
            model_name='classcontent',
            name='class_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_room.ClassRoom'),
        ),
        migrations.AddField(
            model_name='classcontent',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_room.Content'),
        ),
        migrations.AlterUniqueTogether(
            name='present_absent',
            unique_together={('date', 'student', 'class_room')},
        ),
    ]
