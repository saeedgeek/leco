# Generated by Django 3.0.4 on 2020-03-31 00:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('center', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='center',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.expressions.Case, related_name='center', to=settings.AUTH_USER_MODEL),
        ),
    ]
