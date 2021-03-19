# Generated by Django 3.0.5 on 2020-04-23 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.expressions.Case, related_name='teacher', to=settings.AUTH_USER_MODEL),
        ),
    ]