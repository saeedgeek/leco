# Generated by Django 3.0.5 on 2020-04-17 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('class_room', '0001_initial'),
        ('agent', '0002_agent_center'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentclass',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
        migrations.AddField(
            model_name='present_absent',
            name='class_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_room.ClassRoom'),
        ),
        migrations.AddField(
            model_name='present_absent',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='pre_required',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_reuired', to='class_room.Lesson'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='class_room', to='agent.Agent'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='content',
            field=models.ManyToManyField(related_name='class_room', through='class_room.ClassContent', to='class_room.Content'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_room.Lesson'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='student',
            field=models.ManyToManyField(related_name='class_room', through='class_room.StudentClass', to='student.Student'),
        ),
    ]
